import math


class Vector(object):

    def __init__(self, coordinates):
        self.CANNOT_NORMALIIZE_ZERO_VECTOR_MSG = "Cannot normalize a zero vector"

        try:
            if not coordinates:
                raise ValueError

            self.coordinates = tuple([float(v) for v in coordinates])
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
        return 'Vector {}'.format(self.coordinates)

    def __repr__(self):
        return 'Vector {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def magnitude(self):
        return math.sqrt(sum([x ** 2 for x in self.coordinates]))

    def normalized(self):
        try:
            return Vector(self.coordinates) * (1 / self.magnitude())
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIIZE_ZERO_VECTOR_MSG)

    def dot(self, other):
        return sum([x * y for x, y in zip(self.coordinates, other.coordinates)])

    def angle_with(self, other, in_degrees=False):
        try:
            u1 = self.normalized()
            u2 = other.normalized()
            dot_product = u1.dot(u2)

            radians = math.acos(dot_product)

            if in_degrees:
                return radians * (180 / math.pi)
            else:
                return radians

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')
            else:
                raise e
