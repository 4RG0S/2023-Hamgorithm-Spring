import sys

N, M = map(int, sys.stdin.readline().split())


arr = [0] * N
for i in range(N):
    arr[i] = int(sys.stdin.readline().rstrip())
arr.sort()  #수열 정렬

# 투 포인터 이용
l , r = 0, 1 


m = 2000000000


while l < N and r < N:
    a = arr[r] - arr[l]
    if a == M :
        print(M)
        exit(0)

    if a < M :
        r += 1
        continue
    l += 1
    m = min(m , a)
    

print(m)