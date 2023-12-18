from flask import render_template, Blueprint, request, abort, redirect, current_app
from ..forms import CreateProductForm, LogInForm
from ..service import get_goods_list, get_categories_list
from..models import Good, db, Category
from flask_login import login_required, logout_user
import random

bp = Blueprint('bp', __name__, template_folder="bp")


@bp.route('/test')
def test():
    return render_template("bp/home.html")

@bp.route('/')
@bp.route('/dragons')
def dragons():
    data = data=get_goods_list(True, category=1)
    if data is not None:
        return render_template("bp/dragons.html", data=data,  page="dragons")
    return render_template("bp/dragons.html", data=None,  page="dragons")

@bp.route('/california')
def california():
    data = data=get_goods_list(True, category=2)
    if data is not None:
        return render_template("bp/california.html", data=data,  page="california")
    return render_template("bp/california.html", data=None,  page="california")


@bp.route('/maki')
def maki():
    data = data=get_goods_list(True, category=3)
    if data is not None:
        return render_template("bp/maki.html", data=data,  page="maki")
    return render_template("bp/maki.html", data=None,  page="maki")

@bp.route('/drinks')
def drinks():
    data = data=get_goods_list(True, category=4)
    if data is not None:
        return render_template("bp/drinks.html", data=data,  page="drinks")
    return render_template("bp/drinks.html", data=None, page="drinks")

@bp.route('/log_in', methods=['POST', 'GET'])
def log_in():
    form = LogInForm()
    if form.validate_on_submit():
        if form.submit.data:
            print(form.email.data, form.password.data)
    return render_template("bp/log_in.html", form=form)


@bp.route('/add_item/good', methods=['POST', 'GET'])
def add_item():
    form=CreateProductForm()
    if form.validate_on_submit():
        if form.submit.data:
            pass
    return render_template("bp/add_item.html", form=form, page="add_itm")

@bp.route('/add_item/category', methods=['POST', 'GET'])
def add_category():
    form=CreateProductForm()
    if form.validate_on_submit():
        if form.submit.data:
            pass
    return render_template("bp/add_item.html", form=form, page="add_itm")

@bp.route('/admin')
@bp.route('/admin/items')
@login_required
def admin_items():
    print("log_check")
    return render_template("bp/admin.html", page="items")

@bp.route('/api/items')
@login_required
def items_data():
    print("api data")
    query = Good.query

     # search filter
    search = request.args.get('search')
    if search:
        query = query.filter(db.or_(
            Good.name.like(f'%{search}%'),
            Good.description.like(f'%{search}%')
        ))
    total = query.count()

    # sorting
    sort = request.args.get('sort')
    if sort:
        order = []
        for s in sort.split(','):
            direction = s[0]
            name = s[1:]
            if name not in ['name', 'description']:
                name = 'name'
            col = getattr(Good, name)
            if direction == '-':
                col = col.desc()
            order.append(col)
        if order:
            query = query.order_by(*order)
    # pagination
    start = request.args.get('start', type=int, default=-1)
    length = request.args.get('length', type=int, default=-1)
    if start != -1 and length != -1:
        query = query.offset(start).limit(length)
    print("api data end")
    #print([user.to_dict() for user in query])
    print(total)
    # response
    return {
        'data': [user.to_dict() for user in query],
        'total': total,
    }

@bp.route('/api/items', methods=['POST'])
@login_required
def items_update():
    print("api data post")
    data = request.get_json()
    if 'id' not in data:
        abort(400)
    user = Good.query.get(data['id'])
    print("useer before",user)
    for field in ['name', 'description', 'mass', 'price', 'photo']:
        if field in data:
            setattr(user, field, data[field])
    print("useer after", user)
    db.session.commit()
    print("api data post end")
    return '', 204


@bp.route('/admin/categories')
@login_required
def admin_categories():
    print("log_check")
    return render_template("bp/admin_categories.html", page="categories")

@bp.route('/api/categories')
@login_required
def categories_data():
    print("api data")
    query = Category.query

     # search filter
    search = request.args.get('search')
    if search:
        query = query.filter(db.or_(
            Category.name.like(f'%{search}%'),
            Category.items.like(f'%{search}%')
        ))
    total = query.count()

    # sorting
    sort = request.args.get('sort')
    if sort:
        order = []
        for s in sort.split(','):
            direction = s[0]
            name = s[1:]
            if name not in ['name']:
                name = 'name'
            col = getattr(Category, name)
            if direction == '-':
                col = col.desc()
            order.append(col)
        if order:
            query = query.order_by(*order)

    # pagination
    start = request.args.get('start', type=int, default=-1)
    length = request.args.get('length', type=int, default=-1)
    if start != -1 and length != -1:
        query = query.offset(start).limit(length)
    print("api data end")
    data=[category.to_dict() for category in query]
    for category in data:
        print(category.items)
    print("------------------")
    #print(data)
    print(total)
    # response
    return {
        'data': [category.to_dict() for category in query],
        'total': total,
    }

@bp.route('/api/categories', methods=['POST'])
@login_required
def categories_update():
    print("api data post")
    data = request.get_json()
    if 'id' not in data:
        abort(400)
    user = Category.query.get(data['id'])
    for field in ['name']:
        if field in data:
            setattr(user, field, data[field])
    db.session.commit()
    print("api data post end")
    return '', 204


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('dragons')
