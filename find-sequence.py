def check_v(matrix, i, j):
    try:
        if (matrix[i][j] == matrix[i+1][j]) and (matrix[i][j] == matrix[i+2][j]) and \
           (matrix[i][j] == matrix[i+3][j]):
            return True
    except IndexError:
        return False

def check_h(matrix, i, j):
    try:
        if (matrix[i][j] == matrix[i][j+1]) and (matrix[i][j] == matrix[i][j+2]) and \
           (matrix[i][j] == matrix[i][j+3]):
            return True
    except IndexError:
        return False

def check_dd(matrix, i, j):
    try:
        if (matrix[i][j] == matrix[i-1][j-1]) and (matrix[i][j] == matrix[i-2][j-2]) and \
           (matrix[i][j] == matrix[i-3][j-3]):
            if (i-1 < 0)or(i-2 < 0)or(i-3 < 0)or(j-1 < 0)or(j-2 < 0)or(j-3 < 0):
                return False
            return True
    except IndexError:
        return False

def check_du(matrix, i, j):
    try:
        if (matrix[i][j] == matrix[i-1][j+1]) and (matrix[i][j] == matrix[i-2][j+2]) and \
           (matrix[i][j] == matrix[i-3][j+3]):
            if (i-1 < 0)or(i-2 < 0)or(i-3 < 0):
                return False
            return True
    except IndexError:
        return False

def checkio(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if check_v(matrix, i, j) or check_h(matrix, i, j) or \
               check_dd(matrix, i, j) or check_du(matrix, i, j):
                return True
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
