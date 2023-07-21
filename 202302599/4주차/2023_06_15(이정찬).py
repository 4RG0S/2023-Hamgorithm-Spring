A,B = map(int, input().split())
C = []
C0 = []
C1 = []
D = 0

for i in range(B):
    C.append(list(map(int, input().split())))

for i in range(B):
    C0.append(C[i][0])
    C1.append(C[i][1])

C0 = min(C0)
C1 = min(C1)

if A/6 == int(A/6) :
    D = int(A/6)
else :
    D = int(A/6)+1

result1 = C0*(D-1)+C1*(A-(D-1)*6)
result2 = C0*D
result3 = C1*A

result = [result1,result2,result3]

print(min(result))