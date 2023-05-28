import sys
import heapq

n = int(input())
hq = []

for i in range(n):
    m = int(sys.stdin.readline().rstrip())
    if m != 0:
        heapq.heappush(hq, (abs(m), m))
    else:
        if not hq:
            print(0)
        else:
            print(heapq.heappop(hq)[1])