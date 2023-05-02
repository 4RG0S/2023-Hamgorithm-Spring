n, m = map(int, input().split())

result = [0] * n

for _ in range(m):
    a, b, c = map(int, input().split())

    for i in range(a,b+1):
        result[i-1] = c

for i in range(len(result)):
    print(result[i])