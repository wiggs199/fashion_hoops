# New Package 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Set Secret key to protect against cookies when using forms 
app.config['SECRET_KEY'] = '9307f719f3ac67ac0b2e25193fb03f93'
# Specify a relative path from current file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# Database instance 
db = SQLAlchemy(app)

from blog import routes
