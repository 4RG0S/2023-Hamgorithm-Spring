a = input()
b = input()

dp = [[0 for i in range(len(a)+1)] for j in range(len(b)+1)]
for i in range(1, len(b)+1):
    for j in range(1, len(a)+1):
        if b[i-1] == a[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

result = ""
i, j = len(b), len(a)
while i > 0 and j > 0:
    if b[i-1] == a[j-1]:
        result = b[i-1] + result
        i -= 1
        j -= 1
    elif dp[i-1][j] > dp[i][j-1]:
        i -= 1
    else:
        j -= 1

print(dp[-1][-1])
if dp[-1][-1] != 0:
    print(result)