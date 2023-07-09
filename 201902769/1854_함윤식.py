import heapq
import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())

graph = [[] for _ in range(n+1)]
distances = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

heapq.heappush(distances[1], 0)  
q = [(0, 1)]  

while q:
    cost, cur = heapq.heappop(q)
    for next_cost, next_node in graph[cur]:
        new_cost = cost + next_cost
        # k보다 작은 경우 queue에 넣는다.
        if len(distances[next_node]) < k:
            heapq.heappush(distances[next_node], -new_cost)
            heapq.heappush(q, (new_cost, next_node))
        # k보다 큰 경우 queue의 가장 작은 원소와 비교해 더 작은 경우 queue에 넣는다.
        elif distances[next_node] and new_cost < -distances[next_node][0]:
            heapq.heappop(distances[next_node])
            heapq.heappush(distances[next_node], -new_cost)
            heapq.heappush(q, (new_cost, next_node))

for i in range(1, n+1):
    if len(distances[i]) < k:
        print(-1)
    else:
        print(-distances[i][0])
# 1. 다익스트라 알고리즘을 이용하여 1번 노드에서 각 노드까지의 최단거리를 구한다.
# 2. 우선순위 큐를 이용하여 1번 노드에서 각 노드까지의 최단거리를 구한다.