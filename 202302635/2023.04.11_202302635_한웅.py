N = int(input())
ls = list(map(int,input().split()))
M = max(ls)

for i in range(N):
    ls[i] = ls[i] / M * 100

print(sum(ls) / N)