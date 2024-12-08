with open("./day_5/input.in", "r") as file:
    order, lst = file.read().rstrip().split('\n\n')

ans = 0
aux_list = [x.split(',') for x in lst.split('\n')]
flag = True
index_j = []
for j, a in enumerate(aux_list):
    for i in range(1,len(a)):
        trial = '|'.join([a[i-1],a[i]])
        if order.find(trial) == -1:
           flag = False
           index_j.append(j)
    if flag:
        ans += int(a[(len(a)-1)//2])
    else:
        flag = True
        
new_list = [aux_list[i] for i in set(index_j)]
for j,a in enumerate(new_list):
    flag = True
    while flag:
        count = 0
        for i in range(1,len(a)):
            trial = '|'.join([a[i-1],a[i]])
            if order.find(trial) == -1:
                aux = a[i-1]
                a[i-1] = a[i]
                a[i] =aux
                count = 0
            else:
                count += 1
        if count == len(a)-1:
            flag = False



middle_list = [int(new_list[i][(len(new_list[i])-1)//2]) for i in range(len(new_list))]

print(sum(middle_list))


            
