
y=int(input())
x=[[0]*2 for k in range(y)]
length=[0]*y
for k in range(y):
        x[k][0]=input("")
        x[k][1]=len(x[k][0])
x.sort(key=lambda x:(x[1],x[0]))
for k in range(y):
        if(k!=0):
          if(x[k][0]==x[k-1][0]):
            continue
        print("%s"%(x[k][0]))
    
