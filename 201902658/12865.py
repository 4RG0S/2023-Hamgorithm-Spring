if __name__ == "__main__":
    N, W = map(int, input().split())
    input_list = [[0, 0]]
    dp = [[0] * (W + 1) for _ in range(N + 1)]
     
    for _ in range(N):
        input_list.append(list(map(int, input().split())))
    
    for i in range(1, N + 1):
        for j in range(1, W + 1):
            n = input_list[i][0]
            w = input_list[i][1]
            if j < n:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - n] + w)
                
    print(dp[N][W])