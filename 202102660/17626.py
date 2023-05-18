import math

n = int(input())

dp = [i for i in range(n+1)]

for i in range(n+1) :
    for j in range(int(math.sqrt(i))+1):
        if dp[i] > dp[i-j**2]+1 :
            dp[i] = dp[i-j**2]+1

print(dp[n])


