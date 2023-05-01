size = int(input())
arr = [['*' for j in range(size)] for i in range(size)]

def erase(x, y, n):
    if n == 1:
        return
    
    n = int(n/3)
    a = int((n-1)/2)
    x= int(x)
    y = int(y)

    for i in range(-a,a+1):
        for j in range(-a,a+1):
            arr[x+i-1][y+j-1] = ' '

    for i in range(-n,n+1,n):
        for j in range(-n,n+1,n):
            erase(x+i,y+j,n)

erase((size+1)/2, (size+1)/2, size)

for i in range(len(arr)):
    for j in range(len(arr)):
        print(arr[i][j], end = '')
    print()