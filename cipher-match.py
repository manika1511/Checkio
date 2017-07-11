def recall_password(cipher_grille, ciphered_password):
    count = 0
    s = ""
    while count < 4:
        for i in range(0,4):
            for j in range (0,4):
                if cipher_grille[i][j] == 'X':
                    s = s + ciphered_password[i][j]
        rotated = list(zip(*cipher_grille[::-1]))
        cipher_grille = rotated
        count = count + 1

    return s

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
