from flask import Blueprint, request, redirect, url_for, flash, render_template, abort
from flask_login import current_user, login_required
from .. import db
from ..models import Comment, Review, CommentVote
from ..forms import CommentForm
from ..permissions import can_edit_or_delete
from ..utils.filters import clean_text, count_profanities

comments_bp = Blueprint('comments', __name__, url_prefix='/comments')


@comments_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_comment(id):
    comment = Comment.query.get_or_404(id)
    if not can_edit_or_delete(comment):
        abort(403)

    form = CommentForm(obj=comment)
    if form.validate_on_submit():
        cleaned = clean_text(form.content.data)
        if cleaned != form.content.data:
            flash("Twój komentarz zawierał nieodpowiednie słowa i został ocenzurowany.", "warning")
        comment.content = cleaned

        # sprawdzenie liczby wulgaryzmów i ukrycie jeśli za dużo
        count = count_profanities(form.content.data)
        comment.is_hidden = count >= 3

        db.session.commit()
        flash("Komentarz został zaktualizowany.", "success")
        return redirect(url_for('reviews.review_detail', id=comment.review_id))

    return render_template('comments/edit.html', form=form, comment=comment)


@comments_bp.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete_comment(id):
    comment = Comment.query.get_or_404(id)
    if not can_edit_or_delete(comment):
        abort(403)
    
    review_id = comment.review_id
    db.session.delete(comment)
    db.session.commit()
    flash("Komentarz został usunięty.", "success")
    return redirect(url_for('reviews.review_detail', id=review_id))


@comments_bp.route('/<int:id>/upvote', methods=['POST'])
@login_required
def upvote(id):
    comment = Comment.query.get_or_404(id)
    vote = CommentVote.query.filter_by(user_id=current_user.id, comment_id=id).first()

    if vote:
        if vote.value == 1:
            db.session.delete(vote)  # usuń głos
        else:
            vote.value = 1  # zmień z downvote na upvote
    else:
        vote = CommentVote(user_id=current_user.id, comment_id=id, value=1)
        db.session.add(vote)

    db.session.commit()
    return redirect(request.referrer or url_for('reviews.review_detail', id=comment.review_id))


@comments_bp.route('/<int:id>/downvote', methods=['POST'])
@login_required
def downvote(id):
    comment = Comment.query.get_or_404(id)
    vote = CommentVote.query.filter_by(user_id=current_user.id, comment_id=id).first()

    if vote:
        if vote.value == -1:
            db.session.delete(vote)  # usuń głos
        else:
            vote.value = -1  # zmień z upvote na downvote
    else:
        vote = CommentVote(user_id=current_user.id, comment_id=id, value=-1)
        db.session.add(vote)

    db.session.commit()
    return redirect(request.referrer or url_for('reviews.review_detail', id=comment.review_id))
