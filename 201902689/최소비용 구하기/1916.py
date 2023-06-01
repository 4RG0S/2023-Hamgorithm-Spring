import heapq
import sys
input = sys.stdin.readline

INF = float('infinity')
N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
distance = [INF for _ in range(N + 1)]

for _ in range(M):
    a, b, w = map(int, input().split(' '))
    graph[a].append((b, w))

start, end = map(int, input().split(' '))
distance[start] = 0

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        now_dist, now = heapq.heappop(heap)
        # 현재까지 계산한 거리가 현재 cost보다 작으면 다음 원소 확인
        if distance[now] < now_dist:
            continue

        for (next_node, next_weight) in graph[now]:
            if distance[next_node] > now_dist + next_weight:
                distance[next_node] = now_dist + next_weight
                heapq.heappush(heap, (distance[next_node], next_node))

dijkstra(start)
print(distance[end])

