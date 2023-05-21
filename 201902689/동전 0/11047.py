N, K = map(int, input().split(' '))
coins = list(int(input()) for _ in range(N))
coins.sort(reverse=True)
result = 0

while K:
    for coin in coins:
        tmp = K // coin
        if tmp != 0:
            result += tmp
            K = K % coin
            break
        else:
            continue
print(result)