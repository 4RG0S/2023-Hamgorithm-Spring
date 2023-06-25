def dfs(start):
    if len(temp) == m:
        print(*temp)
        return
    for i in range(n):
            temp.append(arr[i])
            dfs(i)
            temp.pop()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
temp = []


dfs(0)