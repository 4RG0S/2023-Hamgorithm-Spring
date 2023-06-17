t = input()
cnt = 0
for _ in range(int(input())):
    s = input()
    if t in s*2:
        cnt += 1
print(cnt)