import unittest
from DiophanticSum import DiophanticSum
from parameterized import parameterized
import util

class TestPrimeTests(unittest.TestCase):
    def setUp(self):
        self.sum = DiophanticSum({"x1": 3, "x2": -1}, 8)
        
    @parameterized.expand([
        [0, 0, +8],
        [1, 0, 11],
        [0, 1, 7],
        [10, -4, 42]
        ])
    def test_evaluateForVariableAssignment(self, x1, x2, expected):
        actual = self.sum.evaluateForVariableAssignment({"x1": x1, "x2": x2})
        self.assertEqual(actual, expected)
        self.assertIsInstance(actual, int)
