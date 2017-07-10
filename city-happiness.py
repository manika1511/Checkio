def most_crucial(net, users):
    l = [] #list of nodes
    d = {} #dict containing nodes and their occurrence in connection
    for connection in net:
        for node in connection:
            l.append(node)
    for item in l:
        if item in d.keys():
            d[item] = d[item] + 1
        else:
            d[item] = 1
    maximum = max(d.values())  # finds the max value
    keys = [x for x, y in d.items() if y == maximum]

    maxx = users[keys[0]]
    most_happy = [keys[0]]
    for item in keys:
        if users[item] > maxx:
            maxx = users[item]
            most_happy[0] = item
        elif users[item] == maxx and item not in most_happy:
            most_happy.append(item)
    return most_happy


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_crucial([
            ['A', 'B'],
            ['B', 'C']
        ],{
            'A': 10,
            'B': 10,
            'C': 10
        }) == ['B'], 'First'

    assert most_crucial([
            ['A', 'B']
        ],{
            'A': 20,
            'B': 10
        }) == ['A'], 'Second'

    assert most_crucial([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['A', 'E']
        ],{
            'A': 0,
            'B': 10,
            'C': 10,
            'D': 10,
            'E': 10
        }) == ['A'], 'Third'

    assert most_crucial([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ],{
            'A': 10,
            'B': 20,
            'C': 10,
            'D': 20
        }) == ['B'], 'Forth'

    print('Nobody expected that, but you did it! It is time to share it!')
