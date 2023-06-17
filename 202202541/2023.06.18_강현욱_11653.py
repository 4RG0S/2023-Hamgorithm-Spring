x=int(input())
key=1
t=x

if(x==1):
    print(end='')
else:
    for i in range(2,t+1):
         for k in range(2,t+1):
             if(x%k==0):
                print(k)
                x=x//k
                break
         if(x==1):
            key=2
            break
        