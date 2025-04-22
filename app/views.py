from flask import Blueprint, render_template, redirect, url_for, request
from .models import Review, Comment, User
from .forms import ReviewForm, CommentForm

reviews_bp = Blueprint('reviews', __name__, url_prefix='/reviews')

@reviews_bp.route('/')
def list_reviews():
    reviews = Review.query.all()
    return render_template('reviews/list.html', reviews=reviews)

@reviews_bp.route('/<int:id>')
def review_detail(id):
    review = Review.query.get_or_404(id)
    form = CommentForm()
    if form.validate_on_submit():
        # obsługa dodawania komentarza
        pass
    return render_template('reviews/detail.html', review=review, form=form)

@reviews_bp.route('/create', methods=['GET', 'POST'])
def create_review():
    form = ReviewForm()
    if form.validate_on_submit():
        # zapisz recenzję i przekieruj
        pass
    return render_template('reviews/create.html', form=form)