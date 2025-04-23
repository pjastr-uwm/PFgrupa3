import pytest
from src.discount import calculate_discounted_price


def test_calculate_correct():
    assert calculate_discounted_price(100, 40) == 60


def test_calculate_negative():
    assert calculate_discounted_price(100, 40) != 50
    assert calculate_discounted_price(40.22, 2.33) != 20.33


def test_invalid_discount():
    with pytest.raises(ValueError):
        calculate_discounted_price(100, "P")