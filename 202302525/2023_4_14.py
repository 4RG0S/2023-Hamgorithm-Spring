x = int(input())

cnt = 0
i = 64

while x != 0:
    while True:
        if x >= i:
            x -= i
            cnt += 1
            break
        else:
            i //= 2

print(cnt)