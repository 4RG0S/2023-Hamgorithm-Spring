n = int(input())
a = 1


for i in range(0, n):
    if n == 1:
        print(1)
    elif n <= a:
        print(i+1)
        break
    else:
        a += 6*(i+1)
