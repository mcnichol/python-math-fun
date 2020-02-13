import os

from flask import Flask, escape, request, redirect, url_for

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


class Vector(object):

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError

            self.coordinates = tuple([float("{0:.3f}".format(v)) for v in coordinates])
            self.dimension = len(coordinates)
        except ValueError:
            raise ValueError('The coordinates must be nonempty')
        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __add__(self, addend):
        return self.__class__(list(map(lambda x, y: x + y, self.coordinates, addend.coordinates)))

    def __sub__(self, subtrahend):
        return self.__class__(list(map(lambda x, y: x - y, self.coordinates, subtrahend.coordinates)))

    def __mul__(self, scalar):
        return self.__class__(list([scalar * x for x in self.coordinates]))

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
