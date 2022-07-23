from flask import Blueprint, render_template


views = Blueprint('views', __name__)


@views.route('/')
def base():
    return render_template("base.html")


@views.route('/login')
def login():
    return render_template("login.html")


@views.route('/sign_up')
def sign_up():
    return render_template("sign_up.html")


if __name__ == '__main__':
    views.run(debug=True)
