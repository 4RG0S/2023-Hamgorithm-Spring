from collections import deque
import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split(' '))
K = int(input())
INF = float('infinity')

graph = [[] for _ in range(V + 1)]
# 가중치 저장을 dictionary
weight = {}
distance = [INF for _ in range(V + 1)]
distance[K] = 0

for _ in range(E):
    u, v, w = map(int, input().split(' '))
    graph[u].append((v, w))

def dijkstra(start):
    queue = []
    # (거리, 노드) 를 저장
    heapq.heappush(queue, (0, start))
    while queue:
        now_dst, now_node = heapq.heappop(queue)
        for node in graph[now_node]:
            next_node, next_weight = node
            if distance[next_node] > now_dst + next_weight:
                distance[next_node] = now_dst + next_weight
                heapq.heappush(queue, (distance[next_node], next_node))


dijkstra(K)
for result in range(1, len(distance)):
    if distance[result] == INF:
        print("INF")
    else: print(distance[result])


# 우선순위 큐를 사용하여 최단거리 먼저 방문하게 하여 불필요하게 갱신하는 것이 없도록 하자