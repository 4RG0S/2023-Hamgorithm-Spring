n = int(input())

dp = [0 for _ in range(1001)]

dp[1] = 1
dp[2] = 2

if n < 3: 
    print(dp[n])
    exit()
def fibo(x):
    if dp[x]:
        return dp[x]
    else:
        dp[x] = fibo(x-1) + fibo(x-2)
        return dp[x]

print(fibo(n) % 10007)