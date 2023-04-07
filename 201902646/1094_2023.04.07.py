stick = int(input())
stick = list(bin(stick))
cnt = 0
for i in range(len(stick)):
    if stick[i] == "1":
        cnt += 1
print(cnt)
