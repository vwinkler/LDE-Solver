from read import read
from LinearDiophanticEquation import LinearDiophanticEquation

equations, _ = read(lambda n: "x{}".format(n))

for equation in equations:
    print(equation)
