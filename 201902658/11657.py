import sys
input = sys.stdin.readline
INF = sys.maxsize

def bellman_ford(start):
    distance[start] = 0
    
    for i in range(1, N + 1):
        for j in range(M):
            now, next, cost = edges[j]
            if distance[now] != INF and distance[next] > distance[now] + cost:
                distance[next] = distance[now] + cost
                if i == N:
                    return True
    return False


N, M = map(int, input().split())
edges = []
distance = [INF] * (N + 1)

for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append([a, b, cost])
    
negative_cycle = bellman_ford(1)

if negative_cycle:
    print(-1)
else:
    for i in range(2, N + 1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])
