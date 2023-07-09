import sys
import heapq

num_operations = int(input())
max_heap = []

for _ in range(num_operations):
    value = int(sys.stdin.readline())
    if value != 0:
        heapq.heappush(max_heap, value)
    else:
        try:
            print(heapq.heappop(max_heap))
        except IndexError:
            print(0)
