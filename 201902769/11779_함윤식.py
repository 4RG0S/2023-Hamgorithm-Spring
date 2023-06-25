import sys, heapq
input = sys.stdin.readline

def dijkstra(n, graph, start, end):
    nearest = [start] * (n + 1)
    distance = [1e9] * (n + 1)

    q = [(0, start)]
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue

        for next, nextDist in graph[now]:
            cost = nextDist + dist
            if cost < distance[next]:
                distance[next], nearest[next] = cost, now
                heapq.heappush(q, (cost, next))

    path = []
    tmp = end
    while tmp != start:
        path.append(str(tmp))
        tmp = nearest[tmp]

    path.append(str(start))
    path.reverse()

    return distance[end], len(path), " ".join(path)


def main():
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    start, end = map(int, input().split())

    shortest_distance, path_length, path = dijkstra(n, m, graph, start, end)

    print(shortest_distance)
    print(path_length)
    print(path)


if __name__ == "__main__":
    main()
