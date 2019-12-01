from math import gcd
from functools import reduce
from util import *
from DiophanticSum import DiophanticSum

class LinearDiophanticEquation:
    def __init__(self):
        self.coefficients = dict()
        self.constant = 0
    def addVariable(self, name, coefficient):
        assert type(coefficient) is int
        self.coefficients[name] = coefficient
    def getCoefficient(self, name):
        return self.coefficients[name]
    def setConstant(self, value):
        assert type(value) is int
        self.constant = value
    def getConstant(self):
        return self.constant
    def isSatisfiable(self):
        if len(self.coefficients) == 0:
            return self.constant == 0
        else:
            divisor = reduce(gcd, self.coefficients.values())
            return (self.constant % divisor == 0)
    def normalize(self):
        assert self.isSatisfiable()
        if len(self.coefficients) > 0:
            divisor = reduce(gcd, self.coefficients.values())
            self.divideByFactor(divisor)
        else:
            self.divideByFactor(self.constant)
    def multiplyWithFactor(self, factor):
        assert type(factor) is int
        if factor == 0:
            self.coefficients = dict()
            self.constant = 0
        else:
            self.coefficients = {key : factor*coeff for key, coeff in self.coefficients.items()}
            self.constant = factor * self.constant
    def divideByFactor(self, divisor):
        assert type(divisor) is int
        assert divisor != 0
        self.coefficients = {key : coeff//divisor for key, coeff in self.coefficients.items()}
        self.constant = self.constant // divisor
    def findVariableWithLowestCoefficientAbsolute(self):
        return min(self.coefficients, key=lambda c: abs(self.coefficients[c]))
    def solveForVariableWithCoefficientOne(self, variableName):
        assert self.coefficients[variableName] == 1
        newCoefficients = {name: -coeff for name, coeff in self.coefficients.items() if name != variableName}
        return DiophanticSum(newCoefficients, self.constant)
    def solveForVariableIntroducingNewVariable(self, variableName, newVariableName):
        m = self.coefficients[variableName] + 1
        newCoefficients = {name: modPrime(coeff, m) for name, coeff in self.coefficients.items() if name != variableName}
        newCoefficients[newVariableName] = -m
        return DiophanticSum(newCoefficients, -modPrime(self.constant, m))
    def insertDiophanticSumForVariable(self, diophanticSum, variable):
        if variable in self.coefficients:
            coeff = self.coefficients[variable]
            newSum = diophanticSum.multiplyWith(coeff)
            self.coefficients.pop(variable)
            self.coefficients = mergeDictionaries(newSum.getCoefficients(), self.coefficients, lambda x, y: x + y)
            self.coefficients = {name: coeff for name, coeff in self.coefficients.items() if coeff != 0}
            self.constant = self.constant - coeff * diophanticSum.getConstant()
            
    def isSolution(self, variableAssignment):
        diophanticSum = DiophanticSum(self.coefficients, -self.constant)
        return (diophanticSum.evaluateForVariableAssignment(variableAssignment) == 0)
    
    def __eq__(self, other):
        if not isinstance(other, LinearDiophanticEquation):
            return NotImplemented
        return self.coefficients == other.coefficients and self.constant == other.constant
    
    def __str__(self):
        return self.__repr__()
    def __repr__(self):
        terms = []
        for name in self.coefficients:
            terms.append(str(self.coefficients[name]) + "*" + str(name))
        lhs = " + ".join(terms)
        if len(self.coefficients) == 0:
            lhs = "0"
        rhs = str(self.constant)
        return lhs + " = " + rhs
