import sys
import heapq

heap = []
for _ in range(int(input())):
    n = int(sys.stdin.readline())
    if n == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap,(-n,n))

