import sys
from read import read
import util
from LinearDiophanticEquation import LinearDiophanticEquation
from LinearDiophanticEquationSystem import LinearDiophanticEquationSystem
from SystemUnsatisfiableException import SystemUnsatisfiableException
import math


equations, numVariables = read(util.makeVariableName)
equationSystem = LinearDiophanticEquationSystem(equations, numVariables, util.makeVariableName)
try:
    solutionForVariables = equationSystem.solve()
    print("SAT")
    print(util.makeSolutionString(solutionForVariables, numVariables, util.makeVariableName))
    #print("correct: {}".format(all([eq.isSolution(variableAssignment) for eq in equations])))
except SystemUnsatisfiableException:
    print("UNSAT")
