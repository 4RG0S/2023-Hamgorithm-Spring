# 백준 2839번 설탕 배달 문제
# DP 문제
# 정답 풀이


N = int(input())


solved = [False] * (5000 + 1)
value = [0] * (5000 + 1)
value[3] = value[5] = 1

def dp(n):
    if n == 0: return 0
    if solved[n]: return value[n]
    ret = 5000
    if n - 3 >= 0:
        ret = min(ret, dp(n - 3) + 1)
    if n - 5 >= 0:
        ret = min(ret, dp(n - 5) + 1)

    solved[n] = True
    value[n] = ret
    return value[n]

result = dp(N)
print(result if result != 5000 else -1)
