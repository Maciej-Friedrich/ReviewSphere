from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename
from .models import Review, Comment, User
from .forms import ReviewForm, CommentForm
from . import db
import os

reviews_bp = Blueprint('reviews', __name__, url_prefix='/reviews')


@reviews_bp.route('/')
def list_reviews():
    reviews = Review.query.all()
    return render_template('reviews/list.html', reviews=reviews)


@reviews_bp.route('/<int:id>', methods=['GET', 'POST'])
def review_detail(id):
    review = Review.query.get_or_404(id)
    comments = Comment.query.filter_by(review_id=id).all()
    form = CommentForm()

    # Obsługa komentarzy
    if form.validate_on_submit() and current_user.is_authenticated:
        new_comment = Comment(
            content=form.content.data,
            user_id=current_user.id,
            review_id=review.id
        )
        db.session.add(new_comment)
        db.session.commit()
        flash("Komentarz został dodany!", "success")
        return redirect(url_for('reviews.review_detail', id=review.id))

    # Obsługa oceny społeczności
    if request.method == "POST" and "community_rating" in request.form:
        if not current_user.is_authenticated:
            flash("Zaloguj się, aby ocenić recenzję.", "warning")
            return redirect(url_for("auth.login"))

        try:
            rating = float(request.form.get("community_rating"))
            if 0.5 <= rating <= 5:
                review.community_rating_sum += rating
                review.community_rating_count += 1
                db.session.commit()
                flash("Dziękujemy za Twoją ocenę!", "success")
                return redirect(url_for('reviews.review_detail', id=review.id))
            else:
                flash("Nieprawidłowa wartość oceny.", "warning")
        except ValueError:
            flash("Wystąpił błąd podczas zapisu oceny.", "danger")

    avg_reviewer_rating = round(review.rating_sum, 1)
    avg_community_rating = round(review.community_rating_sum / review.community_rating_count, 1) if review.community_rating_count else 0

    return render_template(
        'reviews/detail.html',
        review=review,
        form=form,
        comments=comments,
        average_rating=avg_reviewer_rating,
        community_rating=avg_community_rating,
        community_count=review.community_rating_count
    )


@reviews_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_review():
    form = ReviewForm()

    if form.validate_on_submit():
        try:
            rating = float(request.form.get("rating", 0))
            if rating < 0.5 or rating > 5:
                raise ValueError
        except (ValueError, TypeError):
            flash("Wybierz ocenę od 0.5 do 5 gwiazdek.", "warning")
            return render_template('reviews/create.html', form=form)

        image_path = None

        if form.image.data:
            filename = secure_filename(form.image.data.filename)
            image_folder = os.path.join('app', 'static', 'uploads')
            os.makedirs(image_folder, exist_ok=True)
            image_path = os.path.join('uploads', filename)
            form.image.data.save(os.path.join('app', 'static', image_path))

        new_review = Review(
            user_id=current_user.id,
            title=form.title.data,
            content=form.content.data,
            rating_sum=rating,
            rating_count=1,
            image_path=image_path
        )
        db.session.add(new_review)
        db.session.commit()
        flash('Recenzja została dodana!', 'success')
        return redirect(url_for('reviews.list_reviews'))

    return render_template('reviews/create.html', form=form)


@reviews_bp.route('/index')
def root_redirect():
    return redirect(url_for('reviews.list_reviews'))
