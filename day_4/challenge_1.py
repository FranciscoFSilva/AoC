WORD = 'XMAS'
WORD_B = 'SAMX'

with open('./day_4/input.txt','r') as file:
    data = file.read().rstrip()

data = data.split('\n')

count = 0
count_2 = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j:].startswith(WORD):
            count += 1 
        if data[i][j:].startswith(WORD_B):
            count += 1
        if j < len(data[i])-3 and i < len(data)-3 and data[i][j] == 'X' and data[i+1][j+1] == 'M' and data[i+2][j+2] == 'A' and data[i+3][j+3] == 'S':
            count += 1
        if j < len(data[i])-3 and i < len(data)-3 and data[i][j] == 'S' and data[i+1][j+1] == 'A' and data[i+2][j+2] == 'M' and data[i+3][j+3] == 'X':
            count += 1
        if j >= 3 and i < len(data)-3 and data[i][j] == 'X' and data[i+1][j-1] == 'M' and data[i+2][j-2] == 'A' and data[i+3][j-3] == 'S':
            count += 1
        if j >= 3 and i < len(data)-3 and data[i][j] == 'S' and data[i+1][j-1] == 'A' and data[i+2][j-2] == 'M' and data[i+3][j-3] == 'X':
            count += 1
        if i < len(data)-3 and data[i][j] == 'X' and data[i+1][j] == 'M' and data[i+2][j] == 'A' and data[i+3][j] == 'S':
            count += 1
        if i < len(data)-3 and data[i][j] == 'S' and data[i+1][j] == 'A' and data[i+2][j] == 'M' and data[i+3][j] == 'X':
            count += 1
        if j < len(data[i])-2 and i < len(data)-2 and data[i][j] == 'M' and data[i+1][j+1] == 'A' and data[i+2][j+2] == 'S':
            if data[i][j+2] == 'S' and data[i+2][j] == 'M':
                count_2 += 1
            elif data[i][j+2] == 'M' and data[i+2][j] == 'S':
                count_2 += 1
        if j < len(data[i])-2 and i < len(data)-2 and data[i][j] == 'S' and data[i+1][j+1] == 'A' and data[i+2][j+2] == 'M':
            if data[i][j+2] == 'S' and data[i+2][j] == 'M':
                count_2 += 1
            elif data[i][j+2] == 'M' and data[i+2][j] == 'S':
                count_2 += 1


print(count)
print(count_2)