from flask import Blueprint, request, redirect, url_for, flash, render_template, abort
from flask_login import current_user, login_required
from .. import db
from ..models import Comment
from ..forms import CommentForm
from ..permissions import can_edit_or_delete

comments_bp = Blueprint('comments', __name__, url_prefix='/comments')


@comments_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_comment(id):
    comment = Comment.query.get_or_404(id)

    if not can_edit_or_delete(comment):
        abort(403)

    form = CommentForm(obj=comment)

    if form.validate_on_submit():
        comment.content = form.content.data
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
