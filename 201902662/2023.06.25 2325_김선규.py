import heapq
import sys
input = sys.stdin.readline
Inf = float("inf")

def main():
    n, m = map(int, input().split())
    edges = [[] for _ in range(n+1)]
    for _ in range(m):
        x, y, z = map(int, input().split())
        edges[x].append((y, z))
        edges[y].append((x, z))

    def dijkstra(parent, child):
        dist = [Inf for _ in range(n+1)]
        dist[1] = 0
        
        que = [(0, 1)]
        while que:
            d, p = heapq.heappop(que)
            if dist[p] < d: continue

            for c, w in edges[p]:
                if (parent == p and child == c) or (parent == c and child == p): continue
                newDist = d + w
                if dist[c] > newDist:
                    dist[c] = newDist
                    heapq.heappush(que, (newDist, c))
        return dist[n]

    dist = [(Inf, 1, 1) for _ in range(n+1)]
    dist[1] = (0, 1, 1)

    que = [(0, 1)]
    while que:
        d, p = heapq.heappop(que)
        if dist[p][0] < d: continue

        for c, w in edges[p]:
            newDist = d + w
            if dist[c][0] > newDist:
                dist[c] = (newDist, p, c)
                heapq.heappush(que, (newDist, c))

    path = []
    node = n
    while True:
        _, p, c = dist[node]
        path.append((p, c))
        if p == 1: break
        node = p

    dist_max = 0
    for p, c in path:
        value = dijkstra(p, c)
        if value > dist_max:
            dist_max = value
    print(dist_max)

if __name__ == "__main__":
    main()