from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.dialects.sqlite import BLOB
from sqlalchemy.orm import relationship, mapped_column, Mapped
from flask_sqlalchemy import SQLAlchemy
from typing import List

db = SQLAlchemy()


class Category(db.Model):
    __tablename__="categories"
    id      = db.Column(Integer, primary_key=True)
    name    = db.Column(String(30), nullable=False)
    items = db.relationship('Good', backref='categories',
                             lazy='subquery')

class Good(db.Model):
    __tablename__="goods"
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(30), nullable=False)
    description = db.Column(String(360), nullable=False)
    mass = db.Column(Integer, nullable=False)
    price = db.Column(Integer, nullable=False)
    photo = db.Column(String(60), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))
