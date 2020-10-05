import math

inputItems = input().split(' ')
sum = 0
numbers = []
operators = []
isFirst = True

for item in inputItems:
    if item == '*' or item == '/' or item == '+' or item == '-':
        for number in numbers:
            if isFirst:
                sum = int(number)
                isFirst = False
            else:
                if item == '*':
                    sum *= int(number)
                elif item == '/':
                    sum = math.trunc(sum / int(number))
                elif item == '+':
                    sum += int(number)
                else:
                    sum -= int(number)
        numbers = []
    else:
        numbers.append(item)

print(math.trunc(sum))
