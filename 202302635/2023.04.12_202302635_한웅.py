S = input("")
L = list(S)
a = len(S)
S2 = S
tmp = []

for i in range(a//2) :
    tmp = L[i]
    L[i] = L[a-(i+1)]
    L[a-(i+1)] = tmp
L = ''.join(L)

if S2 == L :
    print(1)
else :
    print(0)


