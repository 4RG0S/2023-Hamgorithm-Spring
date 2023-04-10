book, box = map(int, input().split())
if book == 0:
    print(0)
else:
    weight = list(map(int, input().split()))
    temp = 0
    count = 0

    for i in range(len(weight)):
        if weight[i] + temp <= box:
            temp += weight[i]
        elif weight[i] + temp > box:
            temp = 0
            temp += weight[i]
            count += 1
    print(count+1)
