import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgres://uateiulouief8n:p69fcff319c744512f17c8401808374a4ea54f1d1260a64be8f771b0af85bdfaa@ceqbglof0h8enj.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/deltl1lsbe6b4q'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
