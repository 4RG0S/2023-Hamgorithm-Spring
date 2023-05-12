N = int(input())
cnt = N

for i in range(N) :
    a = input()
    for j in range(0, len(a)-1) :
        if a[j] == a[j + 1] :
            pass
        elif a[j] in a[j + 1:] :
            cnt -= 1
            break

print(cnt)