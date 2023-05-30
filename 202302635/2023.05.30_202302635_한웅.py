n = 0
ls = []
while True :
    n = int(input())
    if n == -1 :
        break
    
    for i in range(1,n+1) :
        if n % i == 0 :
            ls.append(i)
    
    if sum(ls[:-1]) != n :
        print(n , "is NOT perfect.")
    else :
        print(n, "=", end=' ')
        for i in range(len(ls)-2) :
            print(ls[i], end=' + ')
        print(ls[-2])

    ls = []

