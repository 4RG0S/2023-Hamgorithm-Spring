n = int(input())
star = [[' ' for j in range((2 * n -1))] for i in range(n)]

for i in range(n):
    for j in range(n-i, n+i+1):
        star[i][j-1] = "*"

def haha(x,y,z):
    if z < 1:
        return
    
    for i in range(z):
        for j in range(z*2- (2*i) -1):
            star[x + i][y + i + j] = ' '

    if z == 3:
        haha(x + z//2, y - 1, z//2)
        haha(x + z//2, y + 5, z//2)
        haha(x - 2, y + 2, z//2)
        
    else:
        haha(x - z//2, y + z//2, z//2)
        haha(x + z//2, y + 3 * (z//2), z//2)
        haha(x + z//2, y - z//2, z//2)

if n == 3:
    haha(n//2, n//2 + 1, n//2)
else:
    haha(n//2, n//2, n//2)

for i in star:
    for j in i:
        print(j, end = '')
    
    print()