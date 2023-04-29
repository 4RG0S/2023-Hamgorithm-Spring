n = int(input())

arr = []
max_dp = list(map(int, input().split()))
min_dp = max_dp.copy()

for i in range(1,n):
    a, b, c = list(map(int, input().split()))
    max_dp = max(max_dp[0], max_dp[1]) + a, max(max_dp[0], max_dp[1], max_dp[2]) + b, max(max_dp[1], max_dp[2]) + c
    min_dp = min(min_dp[0], min_dp[1]) + a, min(min_dp[0], min_dp[1], min_dp[2]) + b, min(min_dp[1], min_dp[2]) + c

print(max(max_dp), min(min_dp))