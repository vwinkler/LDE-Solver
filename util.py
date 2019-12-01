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
