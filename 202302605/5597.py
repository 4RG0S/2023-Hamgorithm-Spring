n, m = map(int, input().split())
arr = [[] for i in range(n)]

for j in range(n):
    arr[j].append(input())

for k in range(n):
    print(arr[k])