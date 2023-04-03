import sys
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
for i in sorted(arr):
    print(i)
