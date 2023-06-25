N, R, C = map(int, input().split())
cnt = 0

while N > 1:
    size = (2 ** N) // 2
    if R < size and C < size:
        pass
    elif R < size <= C:
        cnt += size ** 2
        C -= size
    elif R >= size > C:
        cnt += size ** 2 * 2
        R -= size
    elif R >= size and C >= size:
        cnt += size ** 2 * 3
        R -= size
        C -= size
    N -= 1


if R == 0 and C == 0:
    print(cnt)
if R == 0 and C == 1:
    print(cnt + 1)
if R == 1 and C == 0:
    print(cnt + 2)
if R == 1 and C == 1:
    print(cnt + 3)
