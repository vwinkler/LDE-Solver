import unittest
from LinearDiophanticEquation import LinearDiophanticEquation
from DiophanticSum import DiophanticSum

class ComprehensiveLinearDiophanticEquationTest(unittest.TestCase):
    def setUp(self):
        self.equation = LinearDiophanticEquation()
        self.equation.addVariable("x1", 8)
        self.equation.addVariable("x2", 6)
        self.equation.setConstant(10)
    
    def test_getConstant(self):
        self.assertEqual(self.equation.getConstant(), 10)
    
    def test_getX1Coefficient(self):
        self.assertEqual(self.equation.getCoefficient("x1"), 8)
    
    def test_getX2Coefficient(self):
        self.assertEqual(self.equation.getCoefficient("x2"), 6)
        
    def test_isSatisfiable(self):
        self.assertTrue(self.equation.isSatisfiable())
        
    def test_multiplyWithFactor(self):
        self.equation.multiplyWithFactor(2)
        expected = LinearDiophanticEquation()
        expected.addVariable("x1", 16)
        expected.addVariable("x2", 12)
        expected.setConstant(20)
        self.assertEqual(self.equation, expected)
        
    def test_multiplyWithFactor(self):
        self.equation.divideByFactor(2)
        expected = LinearDiophanticEquation()
        expected.addVariable("x1", 4)
        expected.addVariable("x2", 3)
        expected.setConstant(5)
        self.assertEqual(self.equation, expected)
        
    def test_findVariableWithLowestCoefficientAbsolute(self):
        actual = self.equation.findVariableWithLowestCoefficientAbsolute()
        self.assertEqual(actual, "x2")
        
    def test_solveForVariableIntroducingNewVariable(self):
        actual = self.equation.solveForVariableIntroducingNewVariable("x2", "x3")
        expectedCoefficients = {"x1": 1, "x3": -7}
        expectedConstant = -3
        expected = DiophanticSum(expectedCoefficients, expectedConstant)
        self.assertEqual(actual, expected)
    
    def test_insertDiophanticSumForVariable(self):
        diophanticSum = DiophanticSum({"x4": -2, "x2": 1}, 2)
        expected = LinearDiophanticEquation()
        expected.addVariable("x2", 14)
        expected.addVariable("x4", -16)
        expected.setConstant(-6)
        self.equation.insertDiophanticSumForVariable(diophanticSum, "x1")
        self.assertEqual(self.equation, expected)
