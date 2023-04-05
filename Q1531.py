N, M = map(int, input().split())
result = [[0]*100 for _ in range(100)]
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1-1, x2):
        for j in range(y1-1, y2):
            result[i-1][j-1] += 1
count = 0
for i in range(100):
    for j in range(100):
        if result[i][j] > M:
            count += 1
print(count)
