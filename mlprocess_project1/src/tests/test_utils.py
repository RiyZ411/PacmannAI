
from src.utils.utils import *

def test_is_even_positive():
    expected = True
    actual = is_even(2)

    assert expected == actual

def test_is_even_negative():
    expected = False
    actual = is_even(3)

    assert expected == actual