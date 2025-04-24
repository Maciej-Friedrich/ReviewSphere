# models.py
from . import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.Enum('recenzent', 'moderator', 'admin'), default='recenzent')
    avatar = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha256')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    rating_sum = db.Column(db.Float, default=0)
    rating_count = db.Column(db.Integer, default=0)
    community_rating_sum = db.Column(db.Float, default=0, nullable=False)
    community_rating_count = db.Column(db.Integer, default=0, nullable=False)
    image_path = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    comment_set = db.relationship('Comment', backref='review', lazy=True, cascade="all, delete-orphan")


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review_id = db.Column( db.Integer, db.ForeignKey('review.id', ondelete='CASCADE'),nullable=False  )
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('comments', lazy=True))
    votes = db.relationship('CommentVote', backref='comment', lazy='dynamic')

    @property
    def vote_score(self):
        return sum(v.value for v in self.votes)

class CommunityVote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    review_id = db.Column(db.Integer, db.ForeignKey('review.id'), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (db.UniqueConstraint('user_id', 'review_id', name='_user_review_uc'),)

class CommentVote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'), nullable=False)
    value = db.Column(db.Integer, nullable=False)  # 1 = upvote, -1 = downvote

    __table_args__ = (db.UniqueConstraint('user_id', 'comment_id', name='_user_comment_uc'),)
