import heapq
import sys

read_input = sys.stdin.readline
matrix_size = int(read_input())
heap_list = []

for value in map(int, read_input().split()):
    heapq.heappush(heap_list, value)

for _ in range(1, matrix_size):
    row_values = list(map(int, read_input().split()))
    for row_value in row_values:
        if row_value > heap_list[0]:
            heapq.heappush(heap_list, row_value)
            heapq.heappop(heap_list)

print(heap_list[0])
