n, m = map(int, input().split(' '))
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