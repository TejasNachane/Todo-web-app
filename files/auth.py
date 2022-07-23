from distutils.log import error
from sre_constants import SUCCESS
from flask import Blueprint, flash, render_template
from requests import request

auth = Blueprint('auth', __name__)


@auth.route('/')
def base():
    return render_template("base.html")


@auth.route('/login', methods=['POST,GET'])
def login():
    return render_template("login.html")


@auth.route('/sign_up', methods=['POST,GET'])
def sign_up():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(firstname) < 2:
            flash('Name must be greater than 1 charactor', category=error)
        elif len(lastname) < 4:
            flash('Name must be greater than 3 charactor', category=error)
        elif len(email) < 4:
            flash('Email must be greater than 4 charactor', category=error)
        elif len(password1) < 6:
            flash('Password must be greater than 6 charactor', category=error)
        elif password1 != password2:
            flash('Password don\'t match ', category=error)
        else:
            flash('account created successfully', category=SUCCESS)

    return render_template("sign_up.html")


@auth.route('/logout')
def logout():
    return 'logout page'


if __name__ == '__main__':
    auth.run(debug=True)
