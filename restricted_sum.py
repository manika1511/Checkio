def add(data, total=0):
    if len(data) == 0:
        return total
    return add(data, total + data.pop())

def checkio(data):
    return add(data)
