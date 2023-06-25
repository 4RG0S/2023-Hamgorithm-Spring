import sys
input = sys.stdin.readline
N = int(input())
stairs = []
dp = [0 for _ in range(N)]
for _ in range(N):
    stairs.append(int(input()))

if N <= 2:
    print(sum(stairs))
else:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    for i in range(2, N):
        dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])

    print(dp[-1])
