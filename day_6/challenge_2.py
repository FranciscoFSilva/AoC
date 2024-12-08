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
        og_position = (i, j)

data = [list(x) for x in data]
og_data = data.copy()
count = 0

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == '#':
            continue
        data[i][j] = '#'
        state = set()
        flag = True
        direction = Direction.UP
        position = og_position
        while flag:
            if (position[0],position[1],direction) in state: 
                count +=1
                break
            state.add((position[0],position[1],direction))
            match direction:
                case Direction.UP:
                    if position[0] - 1 < 0:
                        direction = 0
                    elif data[position[0] - 1][position[1]] == '#':
                        direction = Direction.RIGHT
                    else:
                        position = (position[0] - 1, position[1])
                case Direction.RIGHT:
                    if position[1] + 1 >= len(data[0]):
                        direction = 0
                    elif data[position[0]][position[1] + 1] == '#':
                        direction = Direction.DOWN
                    else:
                        position = (position[0], position[1] + 1)
                case Direction.DOWN:
                    if position[0] + 1 >= len(data):
                        direction = 0
                    elif data[position[0] + 1][position[1]] == '#':
                        direction = Direction.LEFT
                    else:
                        position = (position[0] + 1, position[1])
                case Direction.LEFT:
                    if position[1] - 1 < 0:
                        direction = 0
                    elif data[position[0]][position[1] - 1] == '#':
                        direction = Direction.UP
                    else:
                        position = (position[0], position[1] - 1)
                case _:
                    flag = False
        data[i][j] = '.'

print(count)