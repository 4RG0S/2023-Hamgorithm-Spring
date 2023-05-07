n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [[0 for i in range(sum(c) + 1)] for j in range(n)]
dp[0][c[0]:] = [a[0]] * len(dp[0][c[0]:])



for i in range(1, n):
    app, cost = a[i], c[i]
    for j in range(sum(c) + 1):
        if 0 <= j - cost:
            dp[i][j] = max(dp[i-1][j - cost] + app, dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
        
        
for i in range(sum(c) + 1):
    if dp[-1][i] >= m:
        print(i)
        break
    