import math

f = open('input.txt', 'r')
input = int(f.read())

'''
find next perfect odd square
'''


def manhattan_distance(input):
    layer = math.floor(math.ceil(math.sqrt(input)) / 2) + 1
    nextPerfectSquare = (2 * layer - 1) ** 2

    if input >= nextPerfectSquare - layer:
        return layer + nextPerfectSquare - input
    elif input >= nextPerfectSquare - 2 * layer:
        return layer + nextPerfectSquare - input - layer
    elif input >= nextPerfectSquare - 3 * layerlayer:
        return layer + nextPerfectSquare - input - 2 * layer
    else:
        return layer + nextPerfectSquare - input - 3 * layer

print(manhattan_distance(input))
