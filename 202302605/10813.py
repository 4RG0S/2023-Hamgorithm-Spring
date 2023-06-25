n, m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(i+1)

for i in range(m):
    a, b = map(int, input().split())
    arr[a-1], arr[b-1] = arr[b-1], arr[a-1]

for i in arr:
    print(i, end = ' ')