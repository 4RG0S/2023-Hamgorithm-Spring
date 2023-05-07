a = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
b = input()
c = 0

for i in range(len(b)) :
    for j in a :
        if b[i] in j :
            c += a.index(j) + 3
print(c)
