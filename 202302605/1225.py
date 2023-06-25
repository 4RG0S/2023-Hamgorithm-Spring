a, b = input().split()
c = 0

a = list(a)
b = list(b)

for i in a:
    for j in b:
        c += int(i)*int(j)

print(c)