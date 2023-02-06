from flask import Flask, send_file, render_template, abort

import flask

import json

from models import item
from info import get_data, load_data, load_items
import flask_login

app = Flask(__name__)

login_manager = flask_login.LoginManager()

login_manager.init_app(app)

with open("users.json", "r") as f:
    users = json.load(f)


class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return render_template("login.html")

    email = flask.request.form['email']
    if email in users and flask.request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('protected'))

    return 'Bad login'


@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized', 401


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<item_id>")
@flask_login.login_required
def videot(item_id):
    data = get_data(item_id)
    if data.type == "video":
        return render_template(f"video.html", data=data)

    elif data.type == "photo":
        return render_template(f"photo.html", data=data)

    else:
        abort(403)


@app.route("/list")
def list():
    items = load_items()

    return render_template("list.html", items=items)


@app.route("/files/<itemId>")
@flask_login.login_required
def video(itemId):
    data = get_data(itemId)

    return send_file(data.path)


app.run()
