T = int(input())

N = []
for _ in range(T):
    N.append(int(input()))

dp = [0] * (max(N)+1)
dp[0],dp[1],dp[2] = 1,1,1

for i in range(3, max(N)):
    dp[i] = dp[i-2]+dp[i-3]


for elem in N:
    print(dp[elem-1])