import sys


with open('day_8/' + sys.argv[1]) as file:
    data = file.read().strip()


data = data.split('\n')
data = [list(x) for x in data]

R = len(data)
C = len(data[0])

antenna = set()
for i in range(R):
    for j in range(C):
        if data[i][j] != '.':
            antenna.add((i,j,data[i][j]))

count = 0
antenna = list(antenna)
visited = set()
while(antenna):
    fi, fj, fant = antenna.pop()
    flag = False 
    for i, j, ant in antenna:
        if ant == fant:
            flag = True
            di = fi-i
            dj = fj-j
            ni = fi+di
            nj = fj+dj
            while ((ni < R and nj < C) and 
                (ni >= 0 and nj >= 0) and 
                (ni < R and nj >= 0) and 
                (ni >= 0 and nj < C)):
                if (ni, nj) not in visited:
                    visited.add((ni, nj))
                    count += 1  
                ni += di
                nj += dj
            
            ni = fi-di
            nj = fj-dj
            while ((ni < R and nj < C) and 
                (ni >= 0 and nj >= 0) and 
                (ni < R and nj >= 0) and 
                (ni >= 0 and nj < C)):
                if (ni, nj) not in visited:
                    visited.add((ni, nj))
                    count += 1  
                ni -= di
                nj -= dj
            if flag and (fi, fj) not in visited:
                visited.add((fi, fj))
                count += 1

print(count)
