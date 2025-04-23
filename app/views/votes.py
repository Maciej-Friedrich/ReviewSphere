from flask import Blueprint, request, redirect, url_for, flash
from flask_login import current_user, login_required
from ..models import CommunityVote, Review
from .. import db

votes_bp = Blueprint('votes', __name__, url_prefix='/votes')

@votes_bp.route('/<int:review_id>', methods=['POST'])
@login_required
def cast_vote(review_id):
    review = Review.query.get_or_404(review_id)

    if "community_rating" not in request.form:
        flash("Brak oceny.", "warning")
        return redirect(url_for('reviews.review_detail', id=review.id))

    existing_vote = CommunityVote.query.filter_by(user_id=current_user.id, review_id=review.id).first()
    if existing_vote:
        flash("Już oceniłeś tę recenzję.", "info")
        return redirect(url_for('reviews.review_detail', id=review.id))

    try:
        rating = float(request.form.get("community_rating"))
        if 1 <= rating <= 5:
            review.community_rating_sum += rating
            review.community_rating_count += 1

            new_vote = CommunityVote(
                user_id=current_user.id,
                review_id=review.id,
                rating=rating
            )
            db.session.add(new_vote)
            db.session.commit()

            flash("Dziękujemy za Twoją ocenę!", "success")
        else:
            flash("Nieprawidłowa wartość oceny.", "warning")
    except ValueError:
        flash("Wystąpił błąd podczas zapisu oceny.", "danger")

    return redirect(url_for('reviews.review_detail', id=review.id))