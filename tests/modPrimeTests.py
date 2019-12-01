import unittest
from parameterized import parameterized
import util

class TestPrimeTests(unittest.TestCase):
    @parameterized.expand([
        [-5, +1],
        [-4, -1],
        [-3,  0],
        [-2, +1],
        [-1, -1],
        [0,   0],
        [+1, +1],
        [+2, -1],
        [+3,  0],
        [+4, +1],
        [+5, -1]])
    def test(self, a, expected):
        actual = util.modPrime(a, 3)
        self.assertEqual(util.modPrime(a, 3), expected)
        self.assertIsInstance(actual, int)
