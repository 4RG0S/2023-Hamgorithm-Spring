if __name__ == "__main__":
    N, K = map(int, input().split())
    coins = []
    
    for _ in range(N):
        coins.append(int(input()))
        
    count = 0
    coins.sort(reverse = True)
    for coin in coins:
        count += K // coin
        K %= coin
    print(count)