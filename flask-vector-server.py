from flask import Flask, escape, request
import os

app = Flask(__name__)
port = int(os.environ["PORT"])


@app.route('/')
def hello():
  name = request.args.get("name", "World")
  myvector = Vector([1,2,3])
  print(myvector)

  return f'Hello, {escape(name)}!'

@app.route('/add')
def add():
  vector1 = request.args.get("vector1", 0)
  vector2 = request.args.get("vector2", 0)

  vec1 = Vector(list(map(int, vector1.split(","))))
  vec2 = Vector(list(map(int, vector2.split(","))))
    
  return str(vec1 + vec2)

@app.route('/subtract')
def subtract():
  name = request.args.get("name", "World")

  return f'Hello, {escape(name)}!'

@app.route('/multiply')
def multiply():
  name = request.args.get("name", "World")

  return f'Hello, {escape(name)}!'

class Vector(object):
  def __init__(self, coordinates):
    try:
      if not coordinates:
        raise ValueError
      self.coordinates = tuple(coordinates)
      self.dimension = len(coordinates)
    except ValueError:
      raise ValueError('The coordinates must be nonempty')
    except TypeError:
      raise TypeError('The coordinates must be an iterable')
  def __add__(self, addend):
    return self.__class__(list(map(lambda x,y: x+y, self.coordinates,addend.coordinates)))
  def plus(self, addend):
    return self.__class__(list(map(lambda x,y: x+y, self.coordinates,addend.coordinates)))
  def __str__(self):
    return 'Vector: {}'.format(self.coordinates)

  def __eq__(self, v):
    return self.coordinates == v.coordinates


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=port)


