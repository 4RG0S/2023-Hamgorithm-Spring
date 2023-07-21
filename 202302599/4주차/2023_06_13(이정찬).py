A = int(input())
B = [] # list for saving the origin values , deleted for later
C = [] # temp for result
D = [] # temp for saving the result value of C
result = 0
key = 1
for i in range(A) : 
    B.append(list(map(int, input().split())))

for i in range(len(B)) :
    if B[i][0] < 3 or (B[i][0] == 3 and B[i][1] == 1) :
        if len(C) >= 1 :
            if C[0][2] < B[i][2] or (C[0][2] == B[i][2] and C[0][3] < B[i][3]) :
                D.append(B[i]) 
        else : 
            C.append(B[i])

if len(C) == 0 and len(D) == 0 :
    key = 2

temp = 0
if len(D) > 1 :
    for i in range(len(D)-1) :
        if D[temp][2] < D[i+1][2] or (D[temp][2] == D[i+1][2] and D[temp][3] < D[i+1][3]) :
            C = []
            C.append(D[i+1])
            temp = i+1

        else :
            C = []
            C.append(D[temp])

elif len(D) == 0 :
    D = []

else :
    C = []
    C.append(D[temp])

D = []

temp_B = []

for i in range(len(B)) :
    if key == 2 :
        break
    if not ((C[0][2] > B[i][2] or (C[0][2] == B[i][2] and C[0][3] > B[i][3])) and (C[0][0] > B[i][0] or (C[0][0] == B[i][0] and C[0][1] > B[i][1]))):
        temp_B.append(B[i])

B = temp_B[:]
temp_B = []

result += 1

if not(key == 2) :
    while not((C[0][2] > 11) or (C[0][2] == 11 and C[0][3] == 31)) :
        for i in range(len(B)) :
            if B[i][0] < C[0][2] or (B[i][0] == C[0][2] and B[i][1] <= C[0][3]) :
                if C[0][2] < B[i][2] or (C[0][2] == B[i][2] and C[0][3] < B[i][3]) :
                    D.append(B[i])

        if len(D) == 0 :
            key = 2
            break

        temp = 0
        if len(D) > 1 :
            for i in range(len(D)-1) :
                if D[temp][2] < D[i+1][2] or (D[temp][2] == D[i+1][2] and D[temp][3] < D[i+1][3]) :
                    C = []
                    C.append(D[i+1])
                    temp = i+1

                else :
                    C = []
                    C.append(D[temp])
        else :
            C = []
            C.append(D[temp])

        temp_B = []

        for i in range(len(B)) :
            if not((C[0][2] > B[i][2] or (C[0][2] == B[i][2] and C[0][3] > B[i][3])) and (C[0][0] > B[i][0] or (C[0][0] == B[i][0] and C[0][1] > B[i][1]))):
                temp_B.append(B[i])

        B = temp_B[:]
        temp_B = []

        D = []

        result += 1 

if key == 1 :
    print(result)

elif key == 2 :
    print(0)