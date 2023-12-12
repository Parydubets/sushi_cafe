"""
The main module with app initialization
"""

import os
from flask import Flask, render_template
from flask_migrate import Migrate
from sqlalchemy_utils import database_exists,create_database
from .views import bp
from .models import db

print(__name__)


def create_app(test_config=None):
    # create and configure the sushi
    db_user = os.environ.get('DB_USER')
    db_user = str(db_user) + ':'
    db_password = os.environ.get('DB_PASSWORD')
    db_host = os.environ.get('DB_HOST')
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
    @app.route('/home')
    @app.route('/main')
    @app.route('/')
    def hello():
        return render_template("bp/home.html")

    return app
