import pytest

from src.safe_routes import find_safe_routes


def test_returns_three_shortest_distances_sorted():
    distances = [3.5, 1.2, 5.0, 2.1]
    expected = [1.2, 2.1, 3.5]

    assert find_safe_routes(distances) == expected


def test_less_than_three_distances():
    distances = [4.0, 2.0]
    expected = [2.0, 4.0]

    assert find_safe_routes(distances) == expected


def test_distances_already_sorted():
    distances = [0.5, 1.0, 1.5, 2.0]
    expected = [0.5, 1.0, 1.5]

    assert find_safe_routes(distances) == expected


def test_distances_with_equal_values():
    distances = [2.0, 1.0, 1.0, 3.0]
    expected = [1.0, 1.0, 2.0]

    assert find_safe_routes(distances) == expected


def test_empty_list():
    distances = []
    expected = []

    assert find_safe_routes(distances) == expected


if __name__ == "__main__":
    pytest.main([__file__])
