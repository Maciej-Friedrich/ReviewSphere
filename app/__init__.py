import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Inicjalizacja rozszerzeń
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # Gdzie przekierować niezalogowanego użytkownika

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Inicjalizacja rozszerzeń
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Załaduj model użytkownika
    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Zarejestruj blueprinty z folderu views
    from .views.auth import auth_bp
    from .views.reviews import reviews_bp
    from .views.comments import comments_bp
    from .views.votes import votes_bp
    from .views.admin import admin_bp

    app.register_blueprint(admin_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(reviews_bp)
    app.register_blueprint(comments_bp)
    app.register_blueprint(votes_bp)

    # Główna strona przekierowuje do listy recenzji
    @app.route('/')
    def index():
        return redirect(url_for('reviews.list_reviews'))

    return app
