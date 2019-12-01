from SystemUnsatisfiableException import SystemUnsatisfiableException

def lowestCoefficientOfEquation(equation):
    return equation.getCoefficient(equation.findVariableWithLowestCoefficientAbsolute())

class LinearDiophanticEquationSystem:
    def __init__(self, equations, numVariables, makeVariableName):
        self.equations = equations
        self.currentNumVariables = numVariables
        self.makeVariableName = makeVariableName
        self.variableAndAlgebraicSolutionPairs = []
        
    def isIndividuallySatisfiable(self):
        return all([eq.isSatisfiable() for eq in self.equations])
        
    def solve(self):
        if not self.isIndividuallySatisfiable():
            raise SystemUnsatisfiableException()
        else:
            return self.solveWithoutSatisfiabilityCheck()
        
    def solveWithoutSatisfiabilityCheck(self):
        self.normalizeEquations()
        self.simplifyEquationsUntilNoneAreLeft()
        return self.makeBackSubstitution()
    
    def simplifyEquationsUntilNoneAreLeft(self):
        while len(self.equations) > 0:
            self.simplifyEquations()
    
    def simplifyEquations(self):
        currentEquation = self.chooseEquationToTransform() 
        currentVariable = currentEquation.findVariableWithLowestCoefficientAbsolute()
        #print("chosen equation: {}".format(currentEquation))
        #print("chosen variable: {}".format(currentVariable))
        self.simplifyOrEliminateEquation(currentEquation, currentVariable)
        #printEquations(self.equations)
        #print()
    
    def simplifyOrEliminateEquation(self, equation, variable):
        coefficient = equation.getCoefficient(variable)
        if coefficient < 0:
            equation.multiplyWithFactor(-1)

        if abs(coefficient) == 1:
            self.eliminateEquationWithCoefficientlessVariable(equation, variable)
        else:
            self.doEquationTransformationOnVariable(equation, variable)
        self.normalizeEquations() 
    
    def eliminateEquationWithCoefficientlessVariable(self, equation, variable):
        solutionForVariable = equation.solveForVariableWithCoefficientOne(variable)
        self.variableAndAlgebraicSolutionPairs.append((variable, solutionForVariable))
        self.equations.remove(equation)
        self.insertDiophanticSumForVariablesIntoAllEquations(solutionForVariable, variable)
        
    def doEquationTransformationOnVariable(self, equation, variable):
        newVariableName = self.generateNewVariable()
        
        solution = equation.solveForVariableIntroducingNewVariable(variable, newVariableName)
        self.variableAndAlgebraicSolutionPairs.append((variable, solution))
        self.insertDiophanticSumForVariablesIntoAllEquations(solution, variable)
        equation.divideByFactor(solution.getCoefficients()[newVariableName])
    
    def generateNewVariable(self):
        self.currentNumVariables = self.currentNumVariables + 1
        return self.makeVariableName(self.currentNumVariables)
        
    def insertDiophanticSumForVariablesIntoAllEquations(self, diophanticSum, variable):
        for equation in self.equations:
            equation.insertDiophanticSumForVariable(diophanticSum, variable)
        
    def chooseEquationToTransform(self):
        equationWithMinCoeff = min(self.equations, key=lowestCoefficientOfEquation)
        if abs(lowestCoefficientOfEquation(equationWithMinCoeff)) == 1:
            chosenEquation = equationWithMinCoeff
        else:
            chosenEquation = self.equations[0]
        return chosenEquation
        
    def makeBackSubstitution(self):
        solutionForVariables = {}
        for variable, algebraicSolution in reversed(self.variableAndAlgebraicSolutionPairs):
            solution = algebraicSolution.evaluateForVariableAssignment(solutionForVariables)
            solutionForVariables[variable] = solution
        return solutionForVariables
        
    
    def normalizeEquations(self):
        for equation in self.equations:
            equation.normalize()
