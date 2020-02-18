import os

from flask import Flask, request, redirect, url_for, render_template

from db import db
from entity.vector import Vector

app = Flask(__name__)
port = int(os.environ.get("PORT", 8080))


@app.before_first_request
def init_app():
    db.init_db()


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        db.update_message(request.form.get('update_person_text'))
    results = db.get_message()

    return render_template("index.html", person=tuple(results)[len(results) - 1][1])


@app.route('/add')
def add():
    vector1 = request.args.get("vector1", 0)
    vector2 = request.args.get("vector2", 0)

    vec1 = Vector(list(map(float, vector1.split(","))))
    vec2 = Vector(list(map(float, vector2.split(","))))

    return str(vec1 + vec2)


@app.route('/sub')
def sub():
    vector1 = request.args.get("vector1", 0)
    vector2 = request.args.get("vector2", 0)

    vec1 = Vector(list(map(float, vector1.split(","))))
    vec2 = Vector(list(map(float, vector2.split(","))))

    return str(vec1 - vec2)


@app.route('/subtract')
def subtract():
    return redirect(url_for("sub", **request.args))


@app.route('/multiply')
def multiply():
    scalar = float(request.args.get("scalar", 1))
    vector_arg = request.args.get("vector", 0)

    vector = Vector(list(map(float, vector_arg.split(","))))

    return str(vector * scalar)


@app.route('/magnitude')
def magnitude():
    vector = request.args.get("vector", 0)

    vec = Vector(list(map(float, vector.split(","))))

    return vec.magnitude()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
