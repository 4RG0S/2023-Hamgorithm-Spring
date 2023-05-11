n, m = map(int, input().split())

graph = []
visited = []
for _ in range(n+1):
    graph.append([])
    visited.append([False])


for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] != True:
            visited[i] = True
            dfs(i)

cnt = 0

for i in range(1, n+1):
    if visited[i] != True:
        cnt+=1
        dfs(i)

print(cnt)
