import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgres://finance_p2o3_user:sJvdFK4uAmOZCkiWW3OPf26lNAvJkoyM@dpg-cpbakk6n7f5s73f89uj0-a/finance_p2o3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
