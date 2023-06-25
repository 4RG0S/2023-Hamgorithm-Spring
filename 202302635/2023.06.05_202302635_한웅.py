ls = []
x = []
y = []
rx = 0
ry = 0
for i in range(3):
    A = list(map(int,input().split()))
    ls.append(A)
    x.append(ls[i][0])
    y.append(ls[i][1])
for _ in x :
    if x.count(_) == 1 :
        rx = _
for _ in y :
    if y.count(_) == 1:
        ry = _

print(rx, ry)
