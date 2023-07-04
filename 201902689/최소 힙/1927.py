import heapq # 우선순위 큐는 heapq 라이브러리 사용하면 좋다.
import sys
input = sys.stdin.readline
n = int(input())
heap = []

for _ in range(n):
    v = int(input())
    if v == 0:
        # heap이 빈 배열이면 0 출력
        if not heap:
            print(0)
        # heap이 빈 배열이 아니면 heappop()을 통해 꺼내줌
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, v)
