n, m = map(int, input().split())
routers = []

for i in range(n):
    routers.append(int(input()))

routers.sort()

start, end = 1, routers[-1] - routers[0]
ans = start
while start <= end:
    mid = (start + end) // 2
    router_count = 1
    start_idx = 0

    for i in range(1, n):
        wei = routers[i] - routers[start_idx]

        if wei >= mid:
            router_count += 1
            start_idx = i
    
    if router_count >= m:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1
        
print(ans)