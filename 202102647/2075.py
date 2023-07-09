import sys
import heapq

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    for i in arr:
        if len(heap) < N:
            heapq.heappush(heap, i)
        else:
            if heap[0] < i:
                heapq.heappop(heap)
                heapq.heappush(heap, i)
# 메모리 제한으로 인해 N 크기의 배열만으로 비교

print(heap[0])
