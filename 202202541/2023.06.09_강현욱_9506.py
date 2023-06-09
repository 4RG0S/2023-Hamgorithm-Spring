while True:
    x=int(input())
    y=[]
    z=0
    for k in range(1,x):
        if(x % k == 0):
            y.append(k)
            z=z+k
    if(x==z):
        print("%d = 1"%(x),end="")
        p=len(y)
        for j in range(p):
            if(y[j]==1):
                continue
            print(" + %d"%(y[j]),end="")
        print("\n",end="")
    elif(x!=z):
        if(x == -1):
            break
        else:
            print("%d is NOT perfect.\n"%(x),end="")
            y.clear()
    