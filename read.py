import sys
from LinearDiophanticEquation import LinearDiophanticEquation

def read(makeVariableName):
    equations = []
    maxVariableIndex = -1
    for line in sys.stdin.readlines()[1:]:
        coefficientsAndVariables = list(map(int, line.split()[1:-1]))
        
        equation = LinearDiophanticEquation()
        for i in range(0, len(coefficientsAndVariables[:-1]), 2):
            coefficient = coefficientsAndVariables[i]
            name = coefficientsAndVariables[i + 1]
            maxVariableIndex = max(name, maxVariableIndex)
            equation.addVariable(makeVariableName(name), coefficient)
        equation.setConstant(coefficientsAndVariables[-1])
        
        equations.append(equation)
    return equations, maxVariableIndex
