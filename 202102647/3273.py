import sys

a = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
b = int(sys.stdin.readline())
arr.sort()
start, end = 0, a-1
temp = 0
count=0
while start<end:
    temp = arr[start]+arr[end]
    if temp == b:
        count +=1
    if temp < b:
        start+=1
        continue
    end -= 1


print(count)
