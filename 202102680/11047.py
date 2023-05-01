n, k = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))

count = 0
for i in reversed(range(n)):
    count += k//coin[i]
    k = k % coin[i]

print(count)