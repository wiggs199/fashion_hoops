from datetime import datetime
from logging import debug
from typing import DefaultDict
from flask import Flask,render_template,url_for,flash,redirect
from wtforms.validators import Email
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm,LoginForm

app = Flask(__name__)
# Set Secret key to protect against cookies when using forms 
app.config['SECRET_KEY'] = '9307f719f3ac67ac0b2e25193fb03f93'
# Specify a relative path from current file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# Database instance 
db = SQLAlchemy(app)

# Create Columns
class User(db.Model) : 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email= db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20),  nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    post = db.relationship('Post',backref= 'author', lazy=True)

    # MAgic Method used to print object
    def __repr__(self) :
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)

    def __repr__(self) :
        return f"Post('{self.title}','{self.date_posted}')"




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