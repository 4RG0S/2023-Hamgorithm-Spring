while True:
    a, b, c = map(int, input().split(" "))
    if (a, b, c) == (0, 0, 0):
        break
    if a > b:
        if a > c:
            m = a
            n, l = b, c
        else:
            m = c
            n, l = a, b
    else:
        if b > c:
            m, n, l = b, a, c
        else:
            m, n, l = c, a, b

    if (m**2 == (n**2 + l**2)):
        print("right")
    else:
        print("wrong")
