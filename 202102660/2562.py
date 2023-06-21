for i in range(9):
    n = int(input())
    if i == 0:
        max = n
        idx = 1
    elif n > max:
        max = n
        idx = i + 1
print(max)
print(idx)

