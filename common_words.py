def checkio(first, second):
    set1 = set()
    #splitting first at ',' and storing in a set
    set1.update(first.split(','))
    set2 = set()
    # splitting second at ',' and storing in a set
    set2.update(second.split(','))
    #returning a set of the common words
    return (','.join(map(str, sorted(set1.intersection(set2)))))


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
