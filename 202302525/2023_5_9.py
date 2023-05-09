n, m, v = map(int, input().split())
tree = [[] for _ in range(n)]
dfs_result = []
bfs_result = []
bfs_stack = []
floor = 0

for _ in range(m):
    a, b = map(int, input().split())
    tree[a-1].append(b)
    tree[b-1].append(a)

def dfs(v):
    tree[v-1].sort()
    for arg in tree[v-1]:
        if arg in dfs_result:
            continue
        else:
            dfs_result.append(arg)
            dfs(arg)

dfs_result.append(v)
dfs(v)

bfs_result.append(v)
bfs_stack.append(v)
while bfs_stack != []:
    tree[v-1].sort()
    v = bfs_stack[0]
    bfs_stack.remove(v)

    for arg in tree[v-1]:
        if arg in bfs_result:
            continue
        else:
            bfs_stack.append(arg)
            bfs_result.append(arg)

print(*dfs_result)
print(*bfs_result)