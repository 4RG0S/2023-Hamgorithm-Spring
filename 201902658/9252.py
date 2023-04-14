import sys

word1 = sys.stdin.readline()
word2 = sys.stdin.readline()

N = len(word1)
M = len(word2)

dp_table = [[0 for _ in range(M)] for _ in range(N)]

for i in range(1, N):
    for j in range(1, M):
        if word1[i - 1] == word2[j - 1]:
            dp_table[i][j] = dp_table[i - 1][j - 1] + 1
        else:
            dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i][j - 1])

print(dp_table[N - 1][M - 1])

ans = []

x = M - 1
y = N - 1

while x > 0 and y > 0:
    if dp_table[y][x - 1] == dp_table[y][x]:
        x -= 1
    elif dp_table[y - 1][x] == dp_table[y][x]:
        y -= 1
    else:
        ans.append(word1[y - 1])
        x -= 1
        y -= 1
for c in ans[::-1]:
    print(c, end='')
print()
