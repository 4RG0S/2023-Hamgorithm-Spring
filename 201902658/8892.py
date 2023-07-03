from itertools import combinations

test = int(input())

for _ in range(test):
    n = int(input())
    lis = list(input() for i in range(n))
    com = combinations(lis, 2)

    for sa, sb in com:
        add1 = sa+sb
        add2 = sb+sa
        if add1 == add1[::-1]:
            print(add1)
            break
        if add2 == add2[::-1]:
            print(add2)
            break
    else:
        print(0)