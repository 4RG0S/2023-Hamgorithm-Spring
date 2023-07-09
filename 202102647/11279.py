import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x > 0:
        heappush(arr, -x)
    if x == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(-heappop(arr))
