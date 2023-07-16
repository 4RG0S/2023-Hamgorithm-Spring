import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
x = int(input())

start, end = 0, n-1
count = 0

while start < end :
  if arr[start] + arr[end] == x :
    count += 1
    start += 1
  elif arr[start] + arr[end] < x :
    start += 1
  else :
    end -= 1
    
print(count)