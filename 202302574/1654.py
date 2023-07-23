K,N = map(int,input().split())
lines = []
for i in range(K):
    l = int(input())
    lines.append(l)

start = 1
end = max(lines) 

while start <= end:
    cnt = 0
    mid = (start + end) // 2

    for line in lines:
        cnt += line // mid

    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)