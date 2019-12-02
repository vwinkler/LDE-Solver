import sys
from LinearDiophanticEquation import LinearDiophanticEquation

def read(makeVariableName):
    equations = []
    lines = sys.stdin.readlines()
    [numEquations, maxVariableIndex] = map(int, lines[0].split())
    for i in range(1, numEquations + 1):
        line = lines[i]
        splitLine = line.split()
        numTerms = int(splitLine[0]) - 1
        
        equation = LinearDiophanticEquation()
        for i in range(1, numTerms*2 + 1, 2):
            coefficient = int(splitLine[i])
            name = int(splitLine[i + 1])
            equation.addVariable(makeVariableName(name), coefficient)
        equation.setConstant(int(splitLine[numTerms*2 + 1]))
        
        equations.append(equation)
    return equations, maxVariableIndex
