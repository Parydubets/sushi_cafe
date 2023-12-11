from flask import render_template, Blueprint

bp = Blueprint('bp', __name__, template_folder="bp")

@bp.route('/test')
def test():
    return render_template("bp/home.html")

@bp.route('/dragons')
def dragons():
    return render_template("bp/dragons.html")