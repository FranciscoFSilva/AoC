line_1 = []
line_2 = []
with open('day_1/input.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        line_1.append(int(line.rstrip().split('   ')[0]))
        line_2.append(int(line.rstrip().split('   ')[1]))

line_1.sort()
line_2.sort()

distance = sum(list(map(lambda x, y: x - y if x > y else y -x, line_1, line_2)))

print(distance)