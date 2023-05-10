import heapq
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split(' '))
graph = [[] for _ in range(N + 1)]
INF = float('infinity')
# 최단 거리 저장 배열
distance = [INF for _ in range(N + 1)]

# 출발 도시 최단거리를 0으로
distance[X] = 0

heap = []
heapq.heappush(heap, X)

for _ in range(M):
    a, b = map(int, input().split(' '))
    graph[a].append(b)

while heap:
    now = heapq.heappop(heap)
    for index in graph[now]:
        if distance[index] > distance[now] + 1:
            distance[index] = distance[now] + 1
            heapq.heappush(heap, index)

if K not in distance:
    print(-1)
    exit()

for i in range(N+1):
    if K == distance[i]:
        print(i)
