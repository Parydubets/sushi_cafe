"""
The main module with app initialization
"""

import os
from flask import Flask, render_template
from flask_migrate import Migrate
from sqlalchemy_utils import database_exists,create_database
from .views import bp
from .models import db, Category, Good

print(__name__)


def create_app(test_config=None):
    # create and configure the sushi
    db_user = os.environ.get('DB_USER')
    db_user = str(db_user) + ':'
    db_password = os.environ.get('DB_PASSWORD')
    db_host = os.environ.get('DB_HOST')
    db_user='root:'
    db_host='127.0.0.1:3306'
    db_password='admin'
    app = Flask(__name__, instance_relative_config=True)
    database=f'mysql+pymysql://{db_user}{db_password}@{db_host}/sushi'
    print(database)
    if database_exists(database) == False:
        create_database(database)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI=database,

        )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    db.init_app(app)
    app.register_blueprint(bp)
    migrate = Migrate(app, db, directory='sushi/migrations')
    # a simple page that says hello
    @app.cli.command('seed')
    def seed():
        with app.app_context():
            category1 = Category(name="Dragons")
            category2 = Category(name="California")
            category3 = Category(name="Maki")
            category4 = Category(name="Drinks")
            db.session.add(category1)
            db.session.add(category2)
            db.session.add(category3)
            db.session.add(category4)
            set1 = Good(name="Дракон вогняний", description="Норі, Рис, Тигрова креветка, Огірок, Лосось філе, Тобіко (зверху), Сир філа", mass=270, price=197, photo="../static/set1_copy.jpg")
            set2 = Good(name="Дракон зелений", description="Норі, Рис, Сир філа, Вугор, Ікра тобіко, Авокадо, Унагі соус, Кунжут, Огірок", mass=275, price=167, photo="../static/set2_copy.jpg")
            set3 = Good(name="Дракон золотий", description="Норі, Рис, Огірок, Вугор, Тобіко, Сир філа, Тигрова креветка", mass=250, price=182, photo="../static/set3_copy.jpg")
            set4 = Good(name="Філадельфія з вугрем", description="Норі, Рис, Сир філа, Огірок, Вугор, Унагі соус, Кунжут", mass=290, price=191, photo="../static/fila_set_1.jpg")
            set5 = Good(name="Філадельфія з копченим лососем", description="Норі, Рис, Сир філа, Огірок, Копчений лосось", mass=270, price=167, photo="../static/fila_set_2.jpg")
            set6 = Good(name="Філадельфія з тунцем", description="Норі, Рис, Сир філа, Огірок, Тунець, Унагі соус", mass=285, price=163, photo="../static/fila_set_3.jpg")
            category1.items.append(set1)
            category1.items.append(set2)
            category1.items.append(set3)
            category2.items.append(set4)
            category2.items.append(set5)
            category2.items.append(set6)

            db.session.commit()
            return "Seeded successfully"

    return app
