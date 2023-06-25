N = int(input())
ls = []
a = list(map(int,input().split()))
count = 0

for i in range(N) :
    for j in range(1, a[i]+1) :
        if a[i] % j == 0 :
            ls.append(j)
    
    if len(ls) == 2 :
        count += 1
    ls = []
print(count)