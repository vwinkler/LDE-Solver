import sys
from LinearDiophanticEquation import LinearDiophanticEquation

equations = []
for line in sys.stdin.readlines()[1:]:
    coefficientsAndVariables = list(map(int, line.split()[1:-1]))
    
    equation = LinearDiophanticEquation()
    for i in range(0, len(coefficientsAndVariables[:-1]), 2):
        coefficient = coefficientsAndVariables[i]
        name = coefficientsAndVariables[i + 1]
        equation.addVariable("x" + str(name), coefficient)
    equation.setConstant(coefficientsAndVariables[-1])
    
    equations.append(equation)

for equation in equations:
    print(equation)
