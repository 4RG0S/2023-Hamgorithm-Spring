import sys
N,M = map(int,sys.stdin.readline().split())
num = list(map(int,sys.stdin.readline().split()))

dp = [0] * (N+1)
for i in range(N):
    dp[i+1] = dp[i]+num[i]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(dp[j]-dp[i-1])
