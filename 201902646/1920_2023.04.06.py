N = int(input())
A = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))

A.sort()
for i in arr:
    left = 0
    right = len(A)-1
    flag = False
    while left <= right:
        mid = (left+right)//2
        if A[mid] == i:
            flag = True
            print(1)
            break
        elif i > A[mid]:
            left = mid + 1
        elif i < A[mid]:
            right = mid - 1
    if not flag:
        print(0)
