count = 0
with open('day_2/input.txt','r') as file:
    for line in file.readlines():
        report = line.rstrip().split(' ')
        report = list(map(int, report))
        level_diff = [x - report[i - 1] for i, x in enumerate(report)][1:]
        if all(x > 0 for x in level_diff) or all(x < 0 for x in level_diff):
            level_diff = [abs(x) for x in level_diff]
            if all(x >= 1 for x in level_diff) and all(x <= 3 for x in level_diff):
                count += 1

print(count)


