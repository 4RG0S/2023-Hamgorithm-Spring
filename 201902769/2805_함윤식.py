n, m = map(int, input().split())
woods = list(map(int, input().split()))

start, end = 0, max(woods)
ans = start

while start <= end:
    mid = (start + end) // 2
    w = 0
    
    for wood in woods:
        if wood - mid > 0:
            w += wood - mid
    if w >= m:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1
        
        

print(ans)
#  O(n * log max(wood))
# 이진 탐색으로 절단기의 높이를 조정하고, 조정될 때마다 잘린 나무의 길이를 구한다.