N , K = map(int,input().split())
ls = []
for i in range(1,N+1) :
    if N % i == 0 :
        ls.append(i)

if len(ls) < K :
    print(0)
else :
    print(ls[K-1])