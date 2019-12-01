class DiophanticSum:
    def __init__(self, coefficients, constant):
        assert all([type(c) is int for c in coefficients.values()])
        assert type(constant) is int
        self.coefficients = coefficients
        self.constant = constant
    def getConstant(self):
        return self.constant
    def getCoefficients(self):
        return self.coefficients
    def multiplyWith(self, value):
        coefficients = {name : value*coeff for name, coeff in self.coefficients.items()}
        constant = value * self.constant
        return DiophanticSum(coefficients, constant)
    def evaluateForVariableAssignment(self, assignment):
        result = self.constant
        for name in self.coefficients:
            coeff = self.coefficients[name]
            valueOfVariable = assignment[name]
            result = result = coeff*valueOfVariable
        return result
    
    def __eq__(self, other):
        if not isinstance(other, DiophanticSum):
            return NotImplemented
        return self.coefficients == other.coefficients and self.constant == other.constant
    
    def __str__(self):
        return self.__repr__()
    def __repr__(self):
        terms = []
        for name in self.coefficients:
            terms.append(str(self.coefficients[name]) + "*" + str(name))
            
        result = str(self.constant)
        if len(self.coefficients) > 0:
            result = " + ".join(terms) + " + " + result
        return result
