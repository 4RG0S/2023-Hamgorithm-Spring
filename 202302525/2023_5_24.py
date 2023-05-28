n = int(input())
k = list(map(int, input().split()))
k.sort()
result = 100

for i in range(len(k)-1):
    result += k[i]/k[-1] * 100

print(result / n)