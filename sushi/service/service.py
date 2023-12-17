from flask import current_app
from sqlalchemy.sql import func
from ..models import db, Category, Good

def get_categories_list():
    with current_app.app_context():
        data=Category.query.all()
    return data

def get_goods_list(filtration, **kwargs):
    with current_app.app_context():
        if filtration is True:
            data=Good.query.filter(Good.category_id == kwargs["category"]).all()
        else:
            data=Good.query.all()
    return data