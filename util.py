def modPrime(a, b):
    assert type(a) is int
    assert type(b) is int
    assert(b > 0)
    return a - b*((a + b//2)//b)

def mergeDictionaries(a, b, resolveConflict):
    assert type(a) is dict
    assert type(b) is dict
    
    result = dict(a)
    for e in b:
        if e in result:
            result[e] = resolveConflict(result[e], b[e])
        else:
            result[e] = b[e]
    return result

def printEquations(equations):
    for equation in equations:
        print(equation)
        
def printSolutions(solutions):
    for (name, solution) in solutions:
        print("{} = {}".format(name, solution))
        
def makeVariableName(number):
    assert type(number) is int
    return "x{}".format(number)

def makeSolutionString(solutionForVariables, numVariables, makeVariableName): #todo: get rid of numVariables
    output = []
    for i in range(1, numVariables + 1):
        output.append(str(solutionForVariables[makeVariableName(i)]))
    return " ".join(output)
