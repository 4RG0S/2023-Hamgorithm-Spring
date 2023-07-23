n = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()
m = int(input())
keys = list(map(int, input().split(' ')))

def binary_search(key):
    left = 0
    right = n-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return True
        if key < arr[mid]:
            right = mid-1
        elif key > arr[mid]:
            left = mid+1
            
for i in range(m):
    if binary_search(keys[i]):
        print(1)
    else:
        print(0)