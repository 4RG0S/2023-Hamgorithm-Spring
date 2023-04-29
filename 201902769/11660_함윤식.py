import sys
n, m = list(map(int, input().split()))

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(0, n):
    for j in range(1, n):
        arr[i][j] += arr[i][j-1]

for i in range(1, n):
    for j in range(0, n):
        arr[i][j] += arr[i-1][j]


for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1, y1, x2, y2 = x1 - 2, y1 - 2, x2 - 1, y2 - 1
    x2y2 = arr[x2][y2]
    x1y2 = arr[x1][y2] if x1>=0 else 0
    x2y1 = arr[x2][y1] if y1>=0 else 0
    x1y1 = arr[x1][y1] if x1>=0 and y1>=0 else 0
    print(x2y2 - x1y2 - x2y1 + x1y1)