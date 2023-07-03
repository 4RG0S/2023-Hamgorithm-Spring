import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**6)

def bfs(source, sink, parent):
    visited = defaultdict(lambda:0)
    queue = deque()
    queue.append(source)
    visited[source] = 1
    
    while queue:
        u = queue.popleft()
        for i in pipe[u]:
            value = pipe[u][i]
            if visited[i]:
                continue
            if value == 0:
                continue
            queue.append(i)
            visited[i] = 1
            parent[i] = u
            
    if visited[sink]:
        return 1
    else:
        return 0

def ford_fulkerson(source, sink):
    parent = defaultdict(lambda:-1)
    max_flow = 0
    while bfs(source, sink, parent):
        path_flow = sys.maxsize
        s = sink
        while s != source:
            path_flow = min(path_flow, pipe[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            pipe[u][v] -= path_flow
            pipe[v][u] += path_flow
            v = parent[v]
    return max_flow

if __name__ == "__main__":
    N = int(input())
    pipe = defaultdict(lambda:defaultdict(int))
    
    for i in range(N):
        a, b, c = map(str, input().split())
        pipe[a][b] += int(c)
        pipe[b][a] += int(c)
        
    print(ford_fulkerson("A", "Z"))