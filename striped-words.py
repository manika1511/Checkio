VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    text = text.upper()
    for c in ".,?-!":
        text = text.replace(c, " ")
    for c in VOWELS:
        text = text.replace(c, "v")
    for c in CONSONANTS:
        text = text.replace(c, "c")

    words = text.split(" ")

    count = 0
    for word in words:
        if len(word) > 1 and word.isalpha():
            if word.find("cc") == -1 and word.find("vv") == -1:
                count += 1
    return count

if __name__ == '__main__':
    checkio("My name is ...")
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert checkio("My name is ...") == 3, "All words are striped"
    # assert checkio("Hello world") == 0, "No one"
    # assert checkio("A quantity of striped words.") == 1, "Only of"
    # assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
