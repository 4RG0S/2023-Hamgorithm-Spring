n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]

def star(s):
    if s == 3:
        arr[0] = [1, 1, 1]
        arr[1] = [1, 0, 1]
        arr[2] = [1, 1, 1]
        return

    a = s//3
    star(a)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                arr[a*i+k][a*j:a*(j+1)] = arr[k][:a] 

star(n)

for i in arr:
    for j in i:
        if j:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()
