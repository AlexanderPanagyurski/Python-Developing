rows = int(input())
field = [[0 for row in range(rows)] for col in range(rows)]
planeRow = 0
planeCol = 0

for row in range(0, rows):
    line = input().split(' ')
    for col in range(0, rows):
        if line[col] == 'p':
            planeRow = int(row)
            planeCol = int(col)
        field[row][col] = line[col]

commandsCount = int(input())

for i in range(commandsCount):
    commandItems = input().split(' ')
    command = commandItems[0]
    direction = commandItems[1]
    steps = int(commandItems[2])