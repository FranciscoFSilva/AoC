from collections import Counter

line_1 = []
line_2 = []
with open('day_1/input.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        line_1.append(int(line.rstrip().split('   ')[0]))
        line_2.append(int(line.rstrip().split('   ')[1]))

count = Counter(line_2)
sum = 0
for no in line_1:
    sum += count[no]*no

print(sum)