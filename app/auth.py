from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user,logout_user, login_required
from .forms import RegisterForm, LoginForm
from .models import User
from . import db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Rejestracja
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Sprawdź czy istnieje użytkownik z tą nazwą lub emailem
        existing_user = User.query.filter(
            (User.username == form.username.data) | (User.email == form.email.data)
        ).first()

        if existing_user:
            flash('Użytkownik o tej nazwie lub adresie email już istnieje.', 'danger')
            return redirect(url_for('auth.register'))

        # Utwórz nowego użytkownika
        new_user = User(
            username=form.username.data.strip(),
            email=form.email.data.strip(),
            role='recenzent'
        )
        new_user.set_password(form.password.data)  # haszowanie
        db.session.add(new_user)
        db.session.commit()

        flash('Rejestracja zakończona sukcesem! Możesz się teraz zalogować.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', form=form)

# Logowanie
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data.strip()
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Zalogowano pomyślnie.', 'success')
            return redirect(url_for('reviews.list_reviews'))  # zmień, jeśli masz inną stronę główną
        else:
            flash('Nieprawidłowa nazwa użytkownika lub hasło.', 'danger')

    return render_template('auth/login.html', form=form)

# Logout
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Zostałeś wylogowany.', 'info')
    return redirect(url_for('auth.login'))
