from flask import render_template, Blueprint
from ..forms import CreateProductForm, LogInForm
from ..service import get_goods_list, get_categories_list

bp = Blueprint('bp', __name__, template_folder="bp")

@bp.route('/test')
def test():
    return render_template("bp/home.html")

@bp.route('/')
@bp.route('/dragons')
def dragons():
    data = data=get_goods_list(True, category=1)
    if data is not None:
        return render_template("bp/dragons.html", data=data)
    return render_template("bp/dragons.html", data=None)

@bp.route('/california')
def california():
    data = data=get_goods_list(True, category=2)
    if data is not None:
        return render_template("bp/california.html", data=data)
    return render_template("bp/california.html", data=None)


@bp.route('/maki')
def maki():
    data = data=get_goods_list(True, category=3)
    if data is not None:
        return render_template("bp/maki.html", data=data)
    return render_template("bp/maki.html", data=None)

@bp.route('/drinks')
def drinks():
    data = data=get_goods_list(True, category=4)
    if data is not None:
        return render_template("bp/drinks.html", data=data)
    return render_template("bp/drinks.html", data=None)

@bp.route('/log_in', methods=['POST', 'GET'])
def log_in():
    form = LogInForm()
    if form.validate_on_submit():
        if form.submit.data:
            print(form.email.data, form.password.data)
    return render_template("bp/log_in.html", form=form)

@bp.route('/log_check')
def log_check():
    print(get_categories_list())
    print(get_goods_list(False))
    data=get_goods_list(True, category=1)
    print(data)

    return render_template("bp/admin.html")

@bp.route('/add_item', methods=['POST', 'GET'])
def add_item():
    form=CreateProductForm()
    if form.validate_on_submit():
        if form.submit.data:
            pass
    return render_template("bp/add_item.html", form=form)
