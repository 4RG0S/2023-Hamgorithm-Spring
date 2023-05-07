c = [1, 1, 2, 2, 2, 8]
d = input().split()
for i in range(len(c)) :
    c[i] = int(c[i]) - int(d[i])
    print(c[i], end = ' ')