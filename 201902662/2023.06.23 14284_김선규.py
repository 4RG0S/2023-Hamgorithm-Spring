import sys
import heapq
input = sys.stdin.readline
Inf = float("inf")

def main():
    n, m = list(map(int, input().split()))
    edges = {i:{} for i in range(1, n+1)}
    for _ in range(m):
        a, b, c = list(map(int, input().split()))
        edges[a][b] = c
        edges[b][a] = c
    s, t = list(map(int, input().split()))

    dist = [Inf for _ in range(n+1)]
    dist[s] = 0
    
    que = [(0, s)]
    while que:
        d, p = heapq.heappop(que)
        for c in edges[p].keys():
            if dist[c] > d + edges[p][c]:
                dist[c] = d + edges[p][c]
                heapq.heappush(que, (dist[c], c))
    
    print(dist[t])

if __name__ == "__main__":
    main()