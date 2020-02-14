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
    assert actual == expected


def test_get_vector_normalized():
    vector = Vector([5.581, -2.136])

    actual = vector.normalized()

    expected = Vector([.934, -0.357])
    assert actual == expected
