N = int(input())

sol = []

for i in range(2,N+2) :
    while N != 1 :
        if N % i == 0 :
            sol.append(i)
            N = N / i
        else :
            break

for i in range(len(sol)) :
    print(sol[i])