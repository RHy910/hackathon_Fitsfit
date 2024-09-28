import os
class config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '!mypassword!'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'#can be replaced with PostgreSQL, MySQL, etc. as needed
    SQLACHEMY_TRACK_MODIFICATIONS = False