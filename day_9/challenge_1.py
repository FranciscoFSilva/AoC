import sys


# with open('day_9/' + sys.argv[1]) as file:
with open('day_9/' + 'input.in') as file:
    data = file.read().strip()

s = []
id = 0
for i in range(len(data)):
    if i % 2 == 0:
        s += [str(id)]*int(data[i])
        id += 1
    else:
        s += '.'*int(data[i])

print(s)
# with open('file.txt','w') as file:
    # file.write(''.join(s))

# print(''.join(s))
j = len(s) - 1
for i in range(len(s)):
    if s[i] == '.':
        while (s[j] == '.'):
            j -= 1
        s[i] = s[j]
        s[j] = '.'
        j -= 1
        # print(''.join(s))
    if i == j:
        break

# index = s.index('.')
# print([pos for pos, c in enumerate(s[index:]) if c == '.'])
# new_list = list(map(int, s[0:s.index('.')]))
# print(new_list)
print(sum([int(x)*i for i, x in enumerate(s) if x != '.']))