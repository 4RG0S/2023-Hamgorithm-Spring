n, m, r = map(int, input().split())

tree = [[] for _ in range(n)]
visited = [0] * (n)
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    tree[a-1].append(b)
    tree[b-1].append(a)

def dfs(location):
    global cnt
    cnt += 1
    visited[location-1] = cnt
    tree[location-1].sort()

    for i in tree[location-1]: #다음 행선지
        if visited[i-1] == 0:
            dfs(i)

dfs(r)

for i in range(n):
    print(visited[i])