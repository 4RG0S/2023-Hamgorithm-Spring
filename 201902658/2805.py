n, m = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)

while start <= end:
    mid = (start + end) // 2

    log = 0
    for i in tree:
        if i >= mid:
            log += i - mid

    if log >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)