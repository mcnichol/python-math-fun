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