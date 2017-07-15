def fib_no(n):
    fib = [1, 1]
    for i in range(2, n + 1):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def checkio(opacity):
    age = 0
    rem_opacity = 10000
    fib_numbers = fib_no(20) #as the minimum age can be 5000
    while opacity != rem_opacity:
        age += 1
        if age in fib_numbers:
            rem_opacity -= age
        else:
            rem_opacity += 1
    return age

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"