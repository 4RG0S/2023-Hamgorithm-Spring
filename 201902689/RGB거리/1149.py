import sys
input = sys.stdin.readline
N = int(input())

arr = []
for _ in range(N):
    rgb = list(map(int, input().split(' ')))
    arr.append(rgb)

result = []
for i in range(1, N):
    arr[i][0] += min(arr[i-1][1], arr[i-1][2])
    arr[i][1] += min(arr[i-1][0], arr[i-1][2])
    arr[i][2] += min(arr[i-1][0], arr[i-1][1])
print(min(arr[N-1][0], arr[N-1][1], arr[N-1][2]))
