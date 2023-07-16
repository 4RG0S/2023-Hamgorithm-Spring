import sys

B,A = [int(x) for x in sys.stdin.readline().split()]

C = []

D = [] 
temp_D = [1]


result = 0

def tomangto(a,b) :
    C[a][b] = 1
    for i in [-1,1] :
        aa = a+i

        if a == 0 and i == -1 or aa >= A :
            continue

        if C[aa][b] == 0 and not([aa,b] in temp_D):
            temp_D.append([aa,b])
        
    for i in [-1,1] :
        bb = b+i

        if b == 0 and i == -1 or bb >= B :
            continue

        if C[a][bb] == 0 and not([a,bb] in temp_D):
           temp_D.append([a,bb])
           
           

for i in range(A) :
    C.append(list([int(x) for x in sys.stdin.readline().split()]))

for i in range(A) :
    for j in range(B) :
        if C[i][j] == 1 :
            D.append([i,j])
            

while not(len(temp_D) == 0) :
    temp_D = []
    for i in D :
        tomangto(i[0],i[1])
    D = []
    D += temp_D
    result += 1

key = 0

for i in C :
    if 0 in i :
        key = 1 
        break

if key == 0 :
    print(result-1)
elif key == 1 :
    print("-1")

