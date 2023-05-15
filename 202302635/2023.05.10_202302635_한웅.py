C = int(input())



for i in range(C) :
    N = list(map(int,input().split()))
    avg = sum(N[1:]) / N[0]
    cnt = 0
    for j in N[1:] :
        if j > avg :
            cnt += 1

    per = (cnt / N[0]) * 100
    print("%.3f" %per + '%')