class LinearDiophanticEquation:
    def __init__(self):
        self.coefficients = dict()
        self.constant = 0
    def addVariable(self, name, coefficient):
        self.coefficients[name] = coefficient
        
    def getCoefficient(self, name):
        pass
    def setConstant(self, value):
        self.constant = value
    def getConstant(self):
        return self.constant
    def findVariableWithLowestCoefficientAbsolute(self):
        pass
    def solveForVariableWithCoefficientOne(self):
        pass
    def solveForVariableIntroducingNewVariable(self, variableName, newVariableName):
        pass
    def insertDiophanticSum(self, diophanticSum):
        pass
    
    def __str__(self):
        terms = []
        for name in self.coefficients:
            terms.append(str(self.coefficients[name]) + "*" + str(name))
        lhs = " + ".join(terms)
        if len(self.coefficients) == 0:
            lhs = "0"
        rhs = str(self.constant)
        return lhs + " = " + rhs
