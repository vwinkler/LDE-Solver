import unittest
from LinearDiophanticEquation import LinearDiophanticEquation
from DiophanticSum import DiophanticSum

class TrivialEquationTests(unittest.TestCase):
    def setUp(self):
        self.equation = LinearDiophanticEquation()
        self.equation.addVariable("x1", 1)
        self.equation.addVariable("x2", -6)
        self.equation.setConstant(7)
        
    def test_solveForVariableWithCoefficientOne(self):
        actual = self.equation.solveForVariableWithCoefficientOne("x1")
        expectedCoefficients = {"x2": 6}
        expectedConstant = 7
        expected = DiophanticSum(expectedCoefficients, expectedConstant)
        self.assertEqual(actual, expected)
