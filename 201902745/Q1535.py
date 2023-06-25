from sys import stdin

N = int(input())
people = [0] + list(map(int, stdin.readline().split()))
happiness = [0] + list(map(int, stdin.readline().split()))

dp = [[0] * 101 for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, 101):
        if people[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - people[i]] + happiness[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][99])
