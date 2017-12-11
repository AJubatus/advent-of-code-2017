f = open('day1.txt', 'r')
input = f.read()

sum = 0
length = len(input)
halfway = length // 2

firsthalf, secondhalf = input[:halfway], input[halfway:]

for index, value in enumerate(firsthalf):
    if value == secondhalf[index]:
        sum += int(value) * 2

print(sum)
