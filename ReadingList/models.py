from . import db
from flask_login import UserMixin
from sqlalchemy import ForeignKey, Column, String, Integer, CHAR, Boolean




class Books(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    b_title = db.Column(db.String(150))
    b_author = db.Column(db.String(150))
    b_img_src = db.Column(db.String(400))
    b_read = db.Column(db.Boolean, unique = False, default = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150)) 
    name = db.Column(db.String(150))
    books = db.relationship('Books')
