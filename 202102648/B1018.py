import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]

lst = []
for i in range(n-7):
    for j in range(m-7):
        b = 0
        w = 0

        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y)%2==0:
                    if arr[x][y] != 'W':
                        w += 1
                    else:
                        b += 1
                else:
                    if arr[x][y] != 'B':
                        w+=1
                    else:
                        b+=1
        lst.append(w)
        lst.append(b)

print(min(lst))