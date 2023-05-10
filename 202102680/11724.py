import sys

sys.setrecursionlimit(5000)

def DFS(start, depth):
    visited[start] = 1

    for k in graph[start]:
        if visited[k] == 0:
            DFS(k,depth+1)


n, m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
visited = [0] * (n+1)

for i in range(1, n+1):
    if visited[i] == 0:
        if len(graph[i]) == 0:
            visited[i] = 1
            count += 1
        else:
            DFS(i, 0)
            count+=1

print(count)