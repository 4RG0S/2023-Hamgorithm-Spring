from collections import deque

n, m, v = map(int, input().split(' '))

graph = [[] for _ in range(n + 1)]
# visited = [False for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    visited = [False for _ in range(n + 1)]
    stack = [start]
    while stack:
        now = stack.pop()
        if not visited[now]:
            print(now, end=' ')
            visited[now] = True
            graph[now].sort(reverse=True)
        for num in graph[now]:
            if not visited[num]:
                stack.append(num)
    print()

def bfs(start):
    visited = [False for _ in range(n + 1)]
    queue = deque([start])
    while queue:
        now = queue.popleft()
        if not visited[now]:
            print(now, end=' ')
            visited[now] = True
            graph[now].sort(reverse=False)
        for num in graph[now]:
            if not visited[num]:
                queue.append(num)
    print()

dfs(v)
bfs(v)