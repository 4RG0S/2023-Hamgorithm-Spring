import sys
from bisect import bisect_left, bisect
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    v = int(input())
    if v == 0:
        if not heap:
            print(0)
        else:
            # heappush할 때 -를 해서 넣어주었기에 출력시에도 - 해줌
            print(-heapq.heappop(heap))
    else:
        # heapq는 최소 힙으로 구현되어 있어 -를 붙여서 부호 제외하면 최대 힙과 동일
        heapq.heappush(heap, -v)
