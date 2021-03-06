import os


class Config:
    """
    Describes the general configurations
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DATABASE_PASS = os.environ.get('DATABASE_PASS')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kellen:Kellen@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SUBJECT_PREFIX = 'one-minute-pitch'
    SENDER_EMAIL = 'muthonkel@gmail.com'

    # Simple MDE configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    """
    Production configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    pass


class TestConfig(Config):
    """
    Test configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    """
    DATABASE_PASS = os.environ.get('DATABASE_PASS')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kellen:Kellen@localhost/pitch'


class DevConfig(Config):
    """
    Development configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kellen:Kellen@localhost/pitch'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
