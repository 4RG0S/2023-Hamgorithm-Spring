N = int(input())

for i in range(N) :

    for j in range(N-i-1) :
        print(" ", end='')
    for k in range(i*2+1) :
        print("*", end='')
    
    print("")

for i in range(N-1):
    for j in range(i+1) :
        print(" ", end = '')
    for k in range(2*N-2*i-3) :
        print("*", end = '')
    print("")
    

