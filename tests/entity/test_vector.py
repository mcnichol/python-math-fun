from app.entity.vector import Vector


def test_vector_adds():
    vector_1 = Vector([1, 2, 3])
    vector_2 = Vector([1, 2, 3])

    actual = vector_1 + vector_2

    expected = Vector([2, 4, 6])
    assert actual == expected


def test_vector_subtracts():
    vector_1 = Vector([1, 2, 3])
    vector_2 = Vector([1, 2, 3])

    actual = vector_1 - vector_2

    expected = Vector([0, 0, 0])
    assert actual == expected


def test_vector_multiplies_on_scalars():
    vector_1 = Vector([1, 2, 3])
    scalar = 5

    actual = vector_1 * scalar

    expected = Vector([5, 10, 15])
    assert actual == expected


def test_get_vector_magnitude():
    vector = Vector([-0.221, 7.437])

    actual = vector.magnitude()

    expected = 7.44
    assert float("{:.3f}".format(actual)) == expected


def test_get_vector_normalized():
    vector = Vector([5.581, -2.136])

    actual = vector.normalized()

    expected = Vector([.934, -0.357])
    for i in range(vector.dimension):
        assert float("{:.3f}".format(actual.coordinates[i])) == expected.coordinates[i]


def test_get_vector_dot_product():
    v1 = Vector([1, 2, -1])
    v2 = Vector([3, 1, 0])

    actual = v1.angle_with(v2)

    expected = .869
    assert float("{0:.3f}".format(actual)) == expected


def test_get_vector_dot_product_2():
    v1 = Vector([7.887, 4.138])
    v2 = Vector([-8.802, 6.776])

    actual = v1.dot(v2)

    expected = -41.382
    assert float("{0:.3f}".format(actual)) == expected


def test_get_vector_angle_in_radians():
    v1 = Vector([3.183, -7.627])
    v2 = Vector([-2.668, 5.319])

    actual = v1.angle_with(v2)

    expected = 3.072
    assert float("{0:.3f}".format(actual)) == expected


def test_get_vector_angle_in_degrees():
    v1 = Vector([7.35, 0.221, 5.188])
    v2 = Vector([2.751, 8.259, 3.985])

    actual = v1.angle_with(v2, in_degrees=True)

    expected = 60.276
    assert float("{0:.3f}".format(actual)) == expected
