from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.dialects.sqlite import BLOB
from sqlalchemy.orm import relationship, mapped_column, Mapped
from flask_sqlalchemy import SQLAlchemy
from typing import List
from flask_login import UserMixin

db = SQLAlchemy()


class Category(db.Model):
    __tablename__="categories"
    id      = db.Column(Integer, primary_key=True)
    name    = db.Column(String(30), nullable=False)
    items = db.relationship('Good', backref='categories',
                             lazy='subquery')

    def to_dict(self):
        print("items: ", self.items)
        return {
            'id': self.id,
            'name': self.name,
            'items':[item.name+' (id='+str(item.id)+') ' for item in self.items],
        }

class Good(db.Model):
    __tablename__="goods"
    id          = db.Column(Integer, primary_key=True)
    name        = db.Column(String(60), nullable=False)
    description = db.Column(String(360), nullable=False)
    mass        = db.Column(Integer, nullable=False)
    price       = db.Column(Integer, nullable=False)
    photo       = db.Column(String(60), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'mass': self.mass,
            'price': self.price,
            'photo': '<img src="'+self.photo+'">',
            'category_id':self.category_id,
        }

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(1000))
    given_name = db.Column(db.String(500))
    family_name = db.Column(db.String(500))
    accounts = db.Column(db.String(20), default=None)