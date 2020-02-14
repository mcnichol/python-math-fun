import os

from flask import Flask, escape, request, redirect, url_for
from entity.vector import Vector


app = Flask(__name__)
port = int(os.environ.get("PORT", 8080))


@app.route('/')
def hello():
    name = request.args.get("name", "World")

    return f'Hello, {escape(name)}!'


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
