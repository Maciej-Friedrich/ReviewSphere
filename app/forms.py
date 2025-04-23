from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, FileField, SubmitField, PasswordField
from wtforms.validators import DataRequired, NumberRange, Email, EqualTo, Length
from flask_wtf.file import FileAllowed  # ← brakujący import

class LoginForm(FlaskForm):
    username = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    submit = SubmitField('Zaloguj się')


class ReviewForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    content = TextAreaField('Treść', validators=[DataRequired()])
    image = FileField('Obraz', validators=[
        FileAllowed(['jpg', 'jpeg', 'png'], 'Tylko obrazy JPG i PNG!')
    ])  # ← poprawione zamknięcie nawiasu
    submit = SubmitField('Dodaj recenzję')


class CommentForm(FlaskForm):
    content = TextAreaField('Komentarz', validators=[DataRequired()])
    submit = SubmitField('Dodaj komentarz')


class RegisterForm(FlaskForm):
    username = StringField('Nazwa użytkownika', validators=[DataRequired(), Length(min=3, max=50)])
    email = StringField('Adres email', validators=[DataRequired(), Email()])
    password = PasswordField('Hasło', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Potwierdź hasło', validators=[
        DataRequired(), EqualTo('password')
    ])
    submit = SubmitField('Zarejestruj się')
