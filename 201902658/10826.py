if __name__ == "__main__":
    N = int(input())
    
    if N == 0:
        print(0)
        exit()
    if 0 < N <= 2:
        print(1)
        exit()
    
    dp = [0] * (N + 1)
    
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    
    for i in range(3, N + 1):
        dp[i] = (dp[i - 1] + dp[i - 2])
    print(dp[N])