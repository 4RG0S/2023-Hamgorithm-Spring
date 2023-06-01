N = int(input())

li = []
dp = [[0] * N for _ in range(N)]
for i in range(N):
    li.append(list(map(int, input().split())))

dp[0][0] = li[0][0]

for i in range(1, N):
    for j in range(0, i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + li[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + li[i][j]

print(max(dp[N-1]))
