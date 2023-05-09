n = int(input())
count = 0
if n == 1:
    print(1)
elif n < 6:
    print(2)
else:
    i = 1
    while(1):
        if n > 6 * i:
            n -= 6*i
            i += 1
            count += 1
        elif n == 1:
            count += 1
            break
        else:
            count += 2
            break

    print(count