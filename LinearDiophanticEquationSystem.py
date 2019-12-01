from SystemUnsatisfiableException import SystemUnsatisfiableException

def lowestCoefficientOfEquation(equation):
    return equation.getCoefficient(equation.findVariableWithLowestCoefficientAbsolute())

class LinearDiophanticEquationSystem:
    def __init__(self, equations, numVariables, makeVariableName):
        self.equations = equations
        self.currentNumVariables = numVariables
        self.makeVariableName = makeVariableName
    def isIndividuallySatisfiable(self):
        return all([eq.isSatisfiable() for eq in self.equations])
        
    def solve(self):
        if not self.isIndividuallySatisfiable():
            raise SystemUnsatisfiableException()
        else:
            for equation in self.equations:
                equation.normalize()
            
            variableAndAlgebraicSolutionPairs = []

            while len(self.equations) > 0:
                equationWithMinCoeff = min(self.equations, key=lowestCoefficientOfEquation)
                if abs(lowestCoefficientOfEquation(equationWithMinCoeff)) == 1:
                    currentEquation = equationWithMinCoeff
                else:
                    currentEquation = self.equations[0]
                    
                variable = currentEquation.findVariableWithLowestCoefficientAbsolute()
                #print("chosen equation: {}".format(currentEquation))
                #print("chosen variable: {}".format(variable))
                
                coefficient = currentEquation.getCoefficient(variable)
                if coefficient < 0:
                    currentEquation.multiplyWithFactor(-1)

                if abs(coefficient) == 1:
                    solutionForVariable = currentEquation.solveForVariableWithCoefficientOne(variable)
                    variableAndAlgebraicSolutionPairs.append((variable, solutionForVariable))
                    self.equations.remove(currentEquation)
                    for equation in self.equations:
                        equation.insertDiophanticSumForVariable(solutionForVariable, variable)
                else:
                    self.currentNumVariables = self.currentNumVariables + 1
                    newVariableName = self.makeVariableName(self.currentNumVariables)
                    
                    solutionForVariable = currentEquation.solveForVariableIntroducingNewVariable(variable, newVariableName)
                    variableAndAlgebraicSolutionPairs.append((variable, solutionForVariable))
                    for equation in self.equations:
                        equation.insertDiophanticSumForVariable(solutionForVariable, variable)
                    currentEquation.divideByFactor(solutionForVariable.getCoefficients()[newVariableName])
                
                for equation in self.equations:
                    equation.normalize()
                        
                #printEquations(self.equations)
                #print()
            
            solutionForVariables = {}
            for variable, algebraicSolution in reversed(variableAndAlgebraicSolutionPairs):
                solution = algebraicSolution.evaluateForVariableAssignment(solutionForVariables)
                solutionForVariables[variable] = solution
        return solutionForVariables
