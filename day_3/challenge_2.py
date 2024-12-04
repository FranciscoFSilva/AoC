import functools
import operator
import re

ans = 0
with open('./day_3/input.txt','r') as file:
    data = file.read().strip()

enabled = True
for i in range(len(data)):
    if data[i:i+len('do()')] == 'do()':
        enabled = True
    if data[i:i+len("don't()")] == "don't()":
        enabled = False
    if data[i:i+len('mul(')] == 'mul(':
        j = i+4
        while data[j] != ')':
            j += 1
        try:
            x, y = map(int, re.findall('\\d{1,3}', data[i:j+1]))
            if data[j-1] not in '0123456789':
                continue
            if enabled:
                ans += x*y
        except:  # noqa: E722
            pass
print(ans) 

p = re.compile("mul\\((\\d{1,3}),(\\d{1,3})\\)")

count = 0
enabled = True
with open('./day_3/input.txt', 'r') as file:
    lines = file.readlines()
    for string in lines:
        for match in p.finditer(string):
            count += functools.reduce(operator.mul, list(map(int, match.groups())))
            print(count)

print(count)