from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, FileField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class ReviewForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    content = TextAreaField('Treść', validators=[DataRequired()])
    rating = IntegerField('Ocena', validators=[DataRequired(), NumberRange(min=1, max=5)])
    image = FileField('Okładka (jpg/png)')
    submit = SubmitField('Dodaj recenzję')

class CommentForm(FlaskForm):
    content = TextAreaField('Komentarz', validators=[DataRequired()])
    submit = SubmitField('Dodaj komentarz')