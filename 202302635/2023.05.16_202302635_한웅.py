a = []
mn = 0
mr, mc = 0, 0
for i in range(9) :
    N = list(map(int,input().split()))
    a.append(N)
for i in range(9) :
    for j in range(9) :
        if mn <= a[i][j] :
            mr = i + 1
            mc = j + 1
            mn = a[i][j]



print(max(map(max,a)))
print(mr, mc)