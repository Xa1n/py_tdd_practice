import math_func
import pytest

def test_add():
    assert math_func.add(5, 5) == 10
    assert math_func.add(5) == 5

def test_substract():
    assert math_func.subtract(7, 3) == 4
    assert math_func.subtract(3, 7) == -4
    assert math_func.subtract(7) == 7

def test_multiply():
    assert math_func.multiply(100, 5) == 500
    assert math_func.multiply(100) == 100

