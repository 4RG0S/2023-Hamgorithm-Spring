def dijkstra(start, graph):
    heap = []
    distance = [sys.maxsize] * (n+1)
    visit = [False] * (n+1)

    distance[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        dist, node = heapq.heappop(heap)
        if visit[node]:
            continue
        visit[node] = True

        for i in graph[node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

    return distance

n, m, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
reverse_graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    reverse_graph[b].append((a, t))

x_distance = dijkstra(x, reverse_graph)

max_distance = 0
for i in range(1, n+1):
    total_distance = dijkstra(i, graph)[x] + x_distance[i]
    max_distance = max(max_distance, total_distance)

print(max_distance)