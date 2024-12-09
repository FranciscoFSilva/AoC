with open('./day_7/input.in', 'r') as file:
    data = file.read().rstrip().split('\n')

data = [x.split(': ') for x in data]

# print(data)

def rec_fun(result, operands, cumulative):
    addtest = cumulative + operands[0] 
    concattest = int(str(cumulative) + str(operands[0]))
    if cumulative == 0:
        multest =  operands[0] 
    else:
        multest = cumulative * operands[0]
    if operands[1:] == []:
        return result == addtest or result == multest or result == concattest
    else:
        addresult = rec_fun(result,operands[1:], addtest)
        mulresult = rec_fun(result,operands[1:], multest)
        concatresult = rec_fun(result,operands[1:], concattest)
        return addresult or mulresult or concatresult

count = 0
operations = ('+','*')
for line in data:
    result = int(line[0])
    operands = list(map(int,line[1].split(' ')))
    if rec_fun(result,operands,0):
        count += result


print(count)