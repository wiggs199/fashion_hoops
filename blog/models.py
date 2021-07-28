from datetime import datetime
from blog import db



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

#Create Columns
class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)

    def __repr__(self) :
        return f"Post('{self.title}','{self.date_posted}')"



