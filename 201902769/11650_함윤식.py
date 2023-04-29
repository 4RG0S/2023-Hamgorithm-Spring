n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort()

for i in arr:
    print(*i)