n, m = map(int, input().split())
arr = list(map(int, input().split()))
left = 0
right = max(arr)
result = 0

while left <= right:
    count = 0
    mid = (left + right) // 2
    for tree in arr:
        if tree > mid:
            count += (tree - mid)
            if count >= m:
                break
    if count >= m:
        result = mid
        left = mid + 1
    else:
        right = mid - 1
print(result)