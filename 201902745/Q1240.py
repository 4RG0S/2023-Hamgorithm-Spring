import sys
sys.setrecursionlimit(10**9)


def dfs(start, end, distance):
    global count
    if start == end:
        count = distance
        return

    for node, val in tree[start]:
        if not visit[node]:
            visit[node] = True
            dfs(node, end, distance + val)


if __name__ == '__main__':
    N, M = map(int, input().split())
    tree = [[] for _ in range(N+1)]

    for i in range(N-1):
        a, b, c = map(int, input().split())
        tree[a].append([b, c])
        tree[b].append([a, c])

    for i in range(M):
        a, b = map(int, input().split())
        visit = [False] * (N + 1)
        count = 0
        visit[a] = True

        dfs(a, b, 0)
        print(count)
