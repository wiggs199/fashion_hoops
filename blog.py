
from logging import debug
from typing import DefaultDict
from flask import Flask,render_template,url_for,flash,redirect
from wtforms.validators import Email
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm,LoginForm
from models import User,Posts

app = Flask(__name__)
# Set Secret key to protect against cookies when using forms 
app.config['SECRET_KEY'] = '9307f719f3ac67ac0b2e25193fb03f93'
# Specify a relative path from current file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# Database instance 
db = SQLAlchemy(app)




posts = [ 
    {
        'author': 'Author',
        'title' : ' Example1',
        'content': 'Blog Post',
        'date_posted': 'June 10 , 2021'
    },
    {
        'author': 'Author',
        'title' : 'Example2',
        'content': 'Blog Post',
        'date_posted' : 'June 10 , 2021'
    }

]

@app.route("/")
@app.route("/home")

def home():
    return render_template('home.html' , posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/register",methods=['GET', 'POST'])
def register():
    form = RegistrationForm()  
    if form.validate_on_submit() :
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))                      #Access to instance RegistrationForm in template
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()                                  #Access to instance RegistrationForm in template
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__' :
    app.run(debug=True)