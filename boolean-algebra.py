OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    if operation == 'conjunction':
        if x==1 and x==y:
            return int(True)
        else:
            return int(False)
    elif operation == 'disjunction':
        if x==0 and x==y:
            return int(False)
        else:
            return int(True)
    elif operation == 'implication':
        a = not bool(x)
        x = int (a)
        if x==0 and x==y:
            return int(False)
        else:
            return int(True)
    elif operation == 'exclusive':
        if x != y:
            return int(True)
        else:
            return int(False)
    else:
        if x == y:
            return int(True)
        else:
            return int(False)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
