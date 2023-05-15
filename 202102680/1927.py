import sys
import heapq


heap = []
for _ in range(int(input())):
    n = int(sys.stdin.readline())

    if n == 0:
        if len(heap):
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, n)
