def main():
    dp = [5]*50001
    dp[0] = 0
    for i in range(50001):
        for j in range(1, int(i**(1/2)) + 1):
            dp[i] = min(dp[i], 1 + dp[i-j*j])
    n = int(input())
    print(dp[n])
    
if __name__ == '__main__':
    main()