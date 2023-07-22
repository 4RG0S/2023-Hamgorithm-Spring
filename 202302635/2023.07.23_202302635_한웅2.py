
K, N = map(int, input().split())
ls = [int(input()) for i in range(K)]
f, l = 1, max(ls) #이분탐색 첫 위치와 끝 위치

while f <= l: 
    mid = (f + l) // 2 
    cnt = 0 #랜선의 개수 cnt
    for i in ls:
        cnt += i // mid 
        
    if cnt >= N: #랜선의 개수가 분기점
        f = mid + 1
    else:
        l = mid - 1
print(l)