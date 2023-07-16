A, B = map(int, input().split())

C = list(map(int, input().split()))

C = C[1:]

D = []

E = []

result = 0

for i in range(1,A+1) :
    D.append(i)

for i in range(B) :
    E.append(list(map(int, input().split())))
    del E[i][0]

while True :
    a = len(C)
    for i in range(B):
        for j in range(len(E[i])) :
            if E[i][j] in C  :
                for k in range(len(E[i])) :
                    if not( E[i][k] in C ) :
                        C.append(E[i][k])
    if a == len(C) :
        break
    
for i in E :
    key = 0
    for j in C :
        if j in i :
            key = 1
    
    if key == 0 :
        result += 1

print(result)            ㅋ