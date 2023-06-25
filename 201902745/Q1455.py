N, M = map(int, input().split())
src = []
for _ in range(N):
    tmp = []
    for i in input():
        tmp.append(i)
    tmp = list(map(int, tmp))
    src.append(tmp)
cnt = 0
for i in range(N - 1, -1, -1):
    for j in range(M - 1, -1, -1):
        if src[i][j]:
            cnt += 1
            for p in range(i + 1):
                for q in range(j + 1):
                    if src[p][q] == 1:
                        src[p][q] = 0
                    else:
                        src[p][q] = 1
print(cnt)
