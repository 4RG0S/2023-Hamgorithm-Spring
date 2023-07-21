def fact(n) :
    if n == 2 :
        return 2
    elif n == 1 :
        return 1
    elif n == 0 :
        return 1
    else :
        return fact(n-1)*n
        
a = int(input())

for i in range(a) :
    A = list(map(int, input().split()))
    print(fact(A[1]) // (fact(A[1]-A[0])*fact(A[0])))
