import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# inicjalizacja rozszerzeń
db = SQLAlchemy()
migrate = Migrate()

# factory
def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # init extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # rejestracja blueprintów
    from .views import reviews_bp
    app.register_blueprint(reviews_bp)

    return app