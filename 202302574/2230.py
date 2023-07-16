num, m = map(int, input().split())

arr = [0]*num
for i in range(num):
    arr[i] = int(input())

arr.sort()
mn = float('inf')

en = 0
for st in range(num):
    while en < num and arr[en] - arr[st] < m:
        en += 1
    if en == num:
        break
    mn = min(mn, arr[en] - arr[st])

print(mn)
