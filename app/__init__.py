import os
from flask import Flask, render_template
from .views import bp

print(__name__)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',


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
    app.register_blueprint(bp)

    # a simple page that says hello
    @app.route('/home')
    @app.route('/main')
    @app.route('/')
    def hello():
        return render_template("bp/home.html")

    return app