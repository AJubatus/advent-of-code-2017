f = open('input.txt', 'r')
input = f.read()

sum = 0
previous = int(input[-1:])

for i in input:
    print(previous)
    i = int(i)
    if i == previous:
        sum += i
    previous = i

print(sum)
