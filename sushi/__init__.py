"""
The main module with app initialization
"""

import os
from flask import Flask, render_template, request, abort, flash,\
    redirect, url_for, jsonify
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, logout_user
from sqlalchemy_utils import database_exists,create_database
from .views import bp
from .models import db, Category, Good, User
from faker import Faker
import random
from .forms import LogInForm

name = "admin"
email = "sushi.admin.1@gmail.com"
password = "AdminSushi"

print(__name__)
class Admin(UserMixin):
    pass

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
            set7 = Good(name="Дракон червоний", description=" Норі, Рис, Огірок, Тигрова креветка, Сир філа, Авокадо, Тунець, Унагі соус, Ікра тобіко", mass=285, price=163, photo="../static/dragon_set_4.jpg")
            set8 = Good(name="Дракон чорний", description="Норі, Рис, Ікра тобіко, Сир філа, Лосось сирий, Вугор, Унагі соус, Кунжут", mass=290, price=174, photo="../static/dragon_set_5.jpg")
            set9 = Good(name="Філадельфія класична з вугрем", description="Норі, Рис, Сир філа, Вугор, Кунжут, Унагі соус", mass=330, price=261, photo="../static/fila_set_4.jpg")
            set10 = Good(name="Філадельфія класична з копченим лососем", description="Норі, Рис, Сир філа, Х/К", mass=310, price=229, photo="../static/fila_set_5.jpg")
            set11 = Good(name="Філадельфія сезам", description="Норі, Рис, Огірок, Сир філа, Кунжут", mass=235, price=89, photo="../static/fila_set_6.jpg")
            set12 = Good(name="Макі з лососем", description="Норі, Рис, Лосось", mass=120, price=62, photo="../static/maki_set_1.jpg")
            set13 = Good(name="Макі з авокадо", description="Норі, Рис, Авокадо", mass=115, price=49, photo="../static/maki_set_2.jpg")
            set14 = Good(name="Макі з вугрем", description="Норі, Рис, Вугор, Кунжут, Унагі соус", mass=125, price=68, photo="../static/maki_set_3.jpg")
            set15 = Good(name="Макі з манго", description="Норі, Рис, Манго", mass=115, price=55, photo="../static/maki_set_4.jpg")
            set16 = Good(name="Макі з огірком", description="Норі, Рис, Огірок, Кунжут", mass=115, price=41, photo="../static/maki_set_5.jpg")
            set17 = Good(name="Вода негазована", description=" ", mass=500, price=20, photo="../static/drink_1.jpg")
            set18 = Good(name="Пепсі 1 л", description=" ", mass=1000, price=45, photo="../static/drink_2.jpg")
            category1.items.append(set1)
            category1.items.append(set2)
            category1.items.append(set3)
            category1.items.append(set7)
            category1.items.append(set8)
            category2.items.append(set4)
            category2.items.append(set5)
            category2.items.append(set6)
            category2.items.append(set9)
            category2.items.append(set10)
            category2.items.append(set11)
            category3.items.append(set12)
            category3.items.append(set13)
            category3.items.append(set14)
            category3.items.append(set15)
            category3.items.append(set16)
            category4.items.append(set17)
            category4.items.append(set18)

            db.session.commit()
            return "Seeded successfully"

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        print('getting user', User.query.get(id), id)
        return User.query.get(id)



    @app.route('/login', methods=['GET', 'POST'])
    def login():
        # Here we use a class of some kind to represent and validate our
        # client-side form data. For example, WTForms is a library that will
        # handle this for us, and we use a custom LoginForm to validate.
        form = LogInForm()
        if form.validate_on_submit():
            user = User(id=1)
            # Login and validate the user.
            # user should be an instance of your `User` class
            print("The default: ",name, email)
            if(form.email.data == email and form.password.data == password):
                login_user(user)

                flash('Logged in successfully.')
                print('Logged in successfully.')
                print(user)
                next = request.args.get('next')
                # url_has_allowed_host_and_scheme should check if the url is safe
                # for redirects, meaning it matches the request host.
                # See Django's url_has_allowed_host_and_scheme for an example.

                return redirect(next or url_for('bp.admin_items'))
            else:
                print('Not logged.')
                flash('Wrong credentials')
        return render_template('bp/log_in.html', form=form)
    def create_fake_users(n):
        """Generate fake users."""
        print("creating fake")
        faker = Faker()
        for i in range(n):
            user = Good(name=faker.name(),
                        age=random.randint(20, 80),
                        address=faker.address().replace('\n', ', '),
                        phone=faker.phone_number(),
                        email=faker.email())
            db.session.add(user)
        db.session.commit()
        print(f'Added {n} fake users to the database.')

    @app.login_manager.unauthorized_handler
    def unauth_handler():
        return render_template("bp/unautorized.html"), 401
    print("very end")
    return app