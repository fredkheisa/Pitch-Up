import os

  
class Config:
    # the uri for the database
    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://fred:pitchproject@localhost/pitch'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('HEROKU_POSTGRESQL_ROSE_URL')


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}