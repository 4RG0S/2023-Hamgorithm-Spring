n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
top = arr[-1]
low = arr[-1] - m

k = []

while low <= top:
    result = 0
    mid = (low + top) // 2

    for arg in arr:
        if arg >= mid:
            result += (arg - mid)

    if result < m:
        top = mid -1
    
    elif result >= m:
        low = mid + 1
        k.append(mid)

k.sort()
print(k[-1])