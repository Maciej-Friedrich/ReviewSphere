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

    # Zarejestruj blueprints
    from .views import reviews_bp
    app.register_blueprint(reviews_bp)

    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    # Główna strona przekierowuje do listy recenzji
    @app.route('/')
    def index():
        return redirect(url_for('reviews.list_reviews'))

    return app
