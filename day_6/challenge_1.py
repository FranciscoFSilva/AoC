from enum import Enum

class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

with open('./day_6/input.in', 'r') as file:
    data = file.read().rstrip().splitlines()


for i, row in enumerate(data):
    j = row.find('^') 
    if j != -1:
        position = (i, j)

data = [list(x) for x in data]

count = 0
flag = True
state = Direction.UP
while flag:
    if data[position[0]][position[1]] != 'X':
        count += 1
        data[position[0]][position[1]] = 'X'
    match state:
        case Direction.UP:
            if position[0] - 1 < 0:
                state = 0
            elif data[position[0] - 1][position[1]] == '#':
                state = Direction.RIGHT
            else:
                position = (position[0] - 1, position[1])
        case Direction.RIGHT:
            if position[1] + 1 >= len(data[0]):
                state = 0
            elif data[position[0]][position[1] + 1] == '#':
                state = Direction.DOWN
            else:
                position = (position[0], position[1] + 1)
        case Direction.DOWN:
            if position[0] + 1 >= len(data):
                state = 0
            elif data[position[0] + 1][position[1]] == '#':
                state = Direction.LEFT
            else:
                position = (position[0] + 1, position[1])
        case Direction.LEFT:
            if position[1] - 1 < 0:
                state = 0
            elif data[position[0]][position[1] - 1] == '#':
                state = Direction.UP
            else:
                position = (position[0], position[1] - 1)
        case _:
            flag = False

data = list(map(''.join, data))
print('\n'.join(data))
print(count)
