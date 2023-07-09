import heapq
import sys

a = sys.stdin.readline
num = int(a())
heap = []

for _ in range(num) : 
    x = int(a())
    # x가 0일 때, heap이 비어있으면 0 출력 / 아니면 최소 원소 반환
    if x == 0 : 
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else : 
        heapq.heappush(heap, x) # x가 0이 아니면 heap에 추가       
# 0이 주어진 횟수만큼 답이 출력되는 원리?
# 0일 때 분기문 -> 1. 0을 출력하거나 / 2. 최소 원소 출력 