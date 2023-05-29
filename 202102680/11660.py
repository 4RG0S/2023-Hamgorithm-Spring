import sys

n, m = map(int, sys.stdin.readline().split())

num_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n):
    dp[i+1][1] = num_list[i][0]
    for j in range(1, n+1):
        dp[i+1][j] = dp[i+1][j-1]+num_list[i][j-1]

# print(dp)
for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    if (x1,y1) == (x2,y2):
        print(dp[x1][y1]-dp[x1][y1-1])
    else:
        sum = 0
        for i in range(x1,x2+1):
            sum += dp[i][y2] - dp[i][y1 - 1]
        print(sum)
