from flask import Flask, render_template
app = Flask(__name__)


@app.route('/base')
def base():
    return render_template("base.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/sign_up')
def sign_up():
    return render_template("sign_up.html")


if __name__ == '__main__':
    app.run(debug=True,port=3030)



