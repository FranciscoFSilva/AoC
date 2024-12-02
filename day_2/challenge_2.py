failed_reports = []
count = 0

with open('day_2/input.txt','r') as file:
    for line in file.readlines():
        report = list(map(int, line.rstrip().split(' ')))
        good = False
        for j in range(len(report)):
            rep = report[:j] + report[j+1:]
            level_diff = [x - rep[i - 1] for i, x in enumerate(rep)][1:]
            if all(x > 0 for x in level_diff) or all(x < 0 for x in level_diff):
                level_diff = [abs(x) for x in level_diff]
                if all(x >= 1 for x in level_diff) and all(x <= 3 for x in level_diff):
                    good = True
        if good:
            count += 1

print(count)
