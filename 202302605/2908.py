a, b = map(str, input().split())
A = a[2]+a[1]+a[0]
B = b[2]+b[1]+b[0]

c = int(A)
d = int(B)

if c > d:
    print(c)
else:
    print(d)