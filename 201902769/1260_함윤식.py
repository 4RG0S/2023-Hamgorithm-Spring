import collections
n, m, v = map(int, input().split())
edge = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

def dfs(v): # dfs 구현
    visited[v] = 1
    print(v, end=' ')
    for i in sorted(edge[v]):
        if not visited[i]:
            dfs(i)

def bfs(v): # bfs 구현
    q = collections.deque()
    q.append(v)
    visited[v] = 1
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in sorted(edge[v]):
            if not visited[i]:
                q.append(i)
                visited[i] = 1

visited = [0] * (n+1)
dfs(v)
print()
visited = [0] * (n+1)
bfs(v)
print()

#간단한 문제인데 탐색 순서가 고정돼 있어 오히려 어렵네요...
#dfs는 재귀로 구현하고, bfs는 큐로 구현했습니다.