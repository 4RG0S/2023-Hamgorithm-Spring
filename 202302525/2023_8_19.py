n, p, q = map(int, input().split())

dp = {}
dp[0] = 1

def sequence(i):
    global p, q

    if i not in dp:
        dp[i] = sequence(i//p) + sequence(i//q)

    return dp[i]

print(sequence(n))