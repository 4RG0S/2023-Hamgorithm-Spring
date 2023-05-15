N , M = map(int,input().split())
a = [0]*N
for _ in range(N) :
    a[_] = _ + 1

for _ in range(M) :
    i , j , k = map(int,input().split())
    a = a[:i-1] + a[k-1:j] + a[i-1:k-1] + a[j:]
    
for i in a :
    print(i, end = ' ')