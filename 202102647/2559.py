import sys

n,k= map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
start = 0
end = start + k
a = sum(arr[start:end])
list1 = [a]
end += 1
while (end <= n):
    a -= arr[start]
    a += arr[end-1]
    list1.append(a)
    start += 1
    end += 1
    
print(max(list1))