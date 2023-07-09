import sys
import heapq

max_heap = []
operation_count = int(sys.stdin.readline())
for _ in range(operation_count):
  current_input = int(sys.stdin.readline())
  if current_input == 0:
    if len(max_heap) == 0:
      print(0)
    else:
      print(-heapq.heappop(max_heap))
  else:
    heapq.heappush(max_heap, -current_input)