n = int(input())

def fac(n) :
    if n < 1 :
        return 1
    else :
        return n * fac(n - 1)

m = str(fac(n))
cnt = 0

for i in range(len(m) - 1, -1, -1) :
    if m[i] == '0' :
        cnt += 1
    else :
        print(cnt)
        break