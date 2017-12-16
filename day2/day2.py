import string
import itertools


f = open('input.txt', 'r')
input = f.read()


table = []
with open('input.txt') as fp:
    for line in fp:
        table.append(list(map(int, line.split())))

p1 = 0
p2 = 0
for line in table:
    p1 += max(line) - min(line)

    for i in itertools.combinations(line, 2):
        if not max(i) % min(i):
            p2 += max(i) // min(i)

print(p1, p2)
