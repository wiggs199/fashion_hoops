  
from flask import render_template, url_for, flash, redirect
from blog import app
from blog.forms import RegistrationForm, LoginForm
from blog.models import User, Post

# dummy data
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