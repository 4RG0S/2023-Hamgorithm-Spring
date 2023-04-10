N , M = map(int,input().split())
bgn = [i+1 for i in range(N)]

for x in range(M):
    i , j = map(int,input().split())
    bgn[i-1:j] = reversed(bgn[i-1:j])
print(*bgn)