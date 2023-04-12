if __name__ == "__main__":
    N = int(input())
    if N == 1:
        print(2)
        exit()
    elif N == 2:
        print(7)
        exit()
    
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 2
    dp[2] = 7
    
    for i in range(3, N + 1):
        dp[i] = (3 * dp[i - 1] + dp[i - 2] - dp[i - 3]) % 1000000007
    print(dp[N])
     