def min(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1:
        vars = args[0]
    else:
        vars = args[:]
    min = None
    for arg in vars:
        if min is None:
            min = arg
        else:
            if key is not None:
                if key(arg) < key(min):
                    min = arg
            else:
                if arg < min:
                    min = arg
    return min


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1:
        vars = args[0]
    else:
        vars = args[:]
    max = None
    for arg in vars:
        if max is None:
            max = arg
        else:
            if key is not None:
                if key(arg) > key(max):
                    max = arg
            else:
                if arg > max:
                    max = arg
    return max


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
