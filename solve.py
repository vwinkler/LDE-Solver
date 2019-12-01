import sys
from read import read
from LinearDiophanticEquation import LinearDiophanticEquation
import math

def lowestCoefficientOfEquation(equation):
    return equation.getCoefficient(equation.findVariableWithLowestCoefficientAbsolute())

def printEquations(equations):
    for equation in equations:
        print(equation)
        
def makeVariableName(number):
    assert type(number) is int
    return "x{}".format(number)



equations, numVariables = read(makeVariableName)
currentNumVariables = numVariables
satisfiable = all([eq.isSatisfiable() for eq in equations])

if not satisfiable:
    print("UNSAT")
else:
    for equation in equations:
        equation.normalize()
    
    variableAndAlgebraicSolutionPairs = []

    while len(equations) > 0:
        equationWithMinCoeff = min(equations, key=lowestCoefficientOfEquation)
        if abs(lowestCoefficientOfEquation(equationWithMinCoeff)) == 1:
            currentEquation = equationWithMinCoeff
        else:
            currentEquation = equations[0]
            
        variable = currentEquation.findVariableWithLowestCoefficientAbsolute()
        #print("chosen equation: {}".format(currentEquation))
        #print("chosen variable: {}".format(variable))
        
        coefficient = currentEquation.getCoefficient(variable)
        if coefficient < 0:
            currentEquation.multiplyWithFactor(-1)

        if abs(coefficient) == 1:
            solutionForVariable = currentEquation.solveForVariableWithCoefficientOne(variable)
            variableAndAlgebraicSolutionPairs.append((variable, solutionForVariable))
            equations.remove(currentEquation)
            for equation in equations:
                equation.insertDiophanticSumForVariable(solutionForVariable, variable)
        else:
            currentNumVariables = currentNumVariables + 1
            newVariableName = makeVariableName(currentNumVariables)
            
            solutionForVariable = currentEquation.solveForVariableIntroducingNewVariable(variable, newVariableName)
            variableAndAlgebraicSolutionPairs.append((variable, solutionForVariable))
            for equation in equations:
                equation.insertDiophanticSumForVariable(solutionForVariable, variable)
            currentEquation.divideByFactor(solutionForVariable.getCoefficients()[newVariableName])
        
        for equation in equations:
            equation.normalize()
                
        #printEquations(equations)
        #print()
    
    solutionForVariables = {}
    for variable, algebraicSolution in reversed(variableAndAlgebraicSolutionPairs):
        solution = algebraicSolution.evaluateForVariableAssignment(solutionForVariables)
        solutionForVariables[variable] = solution

    output = []
    for i in range(1, numVariables + 1):
        output.append(str(solutionForVariables[makeVariableName(i)]))

    print("SAT")
    print(" ".join(output))
    
    #print("correct: {}".format(all([eq.isSolution(variableAssignment) for eq in equations])))
