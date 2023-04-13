n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n-1

min_count = abs(arr[left] + arr[right])
result = [arr[left], arr[right]]

while left < right:
    cur = arr[left] + arr[right]
    
    if abs(min_count) > abs(cur):
        min_count = cur
        result = [arr[left], arr[right]]
        
    
    if cur < 0:
        left += 1
    else:
        right -= 1
    
print(*result)
    