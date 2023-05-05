n, m = map(int, input().split(' '))
visited = [False] * (n + 1)
result = []

def dfs(start):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    for i in range(start+1, n+1):
        if i not in result:
            result.append(i)
            dfs(i)
            result.pop()
dfs(0)