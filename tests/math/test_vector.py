from src.app.math.vector import Vector


def test_vector_adds():
    vector_1 = Vector([1, 2, 3])
    vector_2 = Vector([1, 2, 3])

    actual = vector_1 + vector_2

    expected = Vector([2, 4, 6])

    assert actual == expected
