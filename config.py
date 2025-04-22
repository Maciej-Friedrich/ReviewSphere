import os
from dotenv import load_dotenv

load_dotenv()  # wczytuje zmienne z .env

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')

# ewentualne klasy dla różnych środowisk:
# class DevelopmentConfig(Config):
#     DEBUG = True