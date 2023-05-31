N, M = map(int, input().split())
A = [list(map(int, list(input()))) for _ in range(N)]
B = [list(map(int, list(input()))) for _ in range(N)]
cnt = 0


def convert(i, j, A):
    for iter_i in range(i, i+3):
        for iter_j in range(j, j+3):
            A[iter_i][iter_j] = 1 - A[iter_i][iter_j]


for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            cnt += 1
            convert(i, j, A)

if A != B:
    print(-1)
else:
    print(cnt)
