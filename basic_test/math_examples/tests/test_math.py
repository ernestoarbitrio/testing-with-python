from src.fibonacci import fib
from src.math_xy import dummy_math_function
import unittest
import pytest


def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(10) == 55

class TestDummyMath(unittest.TestCase):

    def test_dummy_math_function(self):
        self.assertAlmostEqual(dummy_math_function(4), 18.849555, places=5)
        self.assertAlmostEqual(dummy_math_function(5), 31.415926, places=5)
        self.assertEqual(dummy_math_function(0), 0)

def test_integration_math():
    a = fib(3)
    b = dummy_math_function(3)

    assert (b/a) is not None
    assert b > a
    assert isinstance(a, int)
    assert isinstance(b, float)

