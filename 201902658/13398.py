if __name__ == "__main__":
    N = int(input())
    init_list = list(map(int, input().split()))
    
    dp = [[x for x in init_list] for _ in range(2)]
    
    for i in range(1, N):
        dp[0][i] = max(dp[0][i - 1] + init_list[i], dp[0][i])
        dp[1][i] = max(dp[0][i - 1], init_list[i] + dp[1][i - 1])
        
    print(max(max(dp[0]), max(dp[1])))