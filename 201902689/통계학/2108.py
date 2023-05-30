import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

if N == 1:
    print(arr[0])
    print(arr[0])
    print(arr[0])
    print(0)
    exit()

mean = round(sum(arr) / N)
arr.sort()
median = arr[N // 2]
scope = max(arr) - min(arr)
cnt = Counter(arr)
# mode를 구하기 위해 Counter로 개수 튜플에서 상위 2개 얻음
mode = cnt.most_common(2)
if mode[0][1] == mode[1][1]:
    mode = mode[1][0]
else: mode = mode[0][0]
print(mean)
print(median)
print(mode)
print(scope)
