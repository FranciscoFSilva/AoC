import functools
import operator
import re

p = re.compile("mul\\((\\d{1,3}),(\\d{1,3})\\)")

count = 0
with open('./day_3/input.txt', 'r') as file:
    lines = file.readlines()
    for string in lines:
        for match in p.finditer(string):
            count += functools.reduce(operator.mul, list(map(int, match.groups())))
            print(count)

print(count)