import sys

def dfs(idx, result):
    global finish
    if finish or result > sum:
        return
    if idx == N:
        if sum == result:
            for i in range(N):
                print(ans[i], end=" ")
            finish = True
        return
    for i in range(1, N+1):
        if not check[i]:
            check[i] = True
            ans[idx] = i
            dfs(idx+1, result + mul[idx] * i)
            if finish:
                break
            check[i] = False

N, sum = map(int, sys.stdin.readline().split())

factorial = [0] * N
mul = [0] * N
check = [False] * (N+1)
ans = [0] * N
factorial[0] = 1
for i in range(1, N):
    factorial[i] = factorial[i-1] * i

for i in range(N):
    mul[i] = factorial[N - 1] // (factorial[N - 1 - i] * factorial[i])
finish = False
dfs(0, 0)
