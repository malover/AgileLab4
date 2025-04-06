import pytest
from Lab4.math_utils import is_even


def test_even_number():
    assert is_even(2) == True


def test_odd_number():
    assert is_even(3) == False


def test_zero():
    assert is_even(0) == True
