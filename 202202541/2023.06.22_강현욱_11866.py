x,y=list(map(int, input().split()))
z=[]
w=[]
for i in range(x):
    z.append(i+1)
j=y-1
key=0
while True:
    if(j>=len(z)):
        while True:
            j=j-len(z)
            if(j<len(z)):
                break
    w.append(z[j])
    del z[j]
    j=j+y-1
    if(len(z)==0):
        break
if(len(w)!=1):   
    for i in range(x):
        if(i==0):
            print("<%d, "%(w[i]),end='')
        elif(i==x-1):
            print("%d>"%(w[i]))
        else:
            print("%d, "%(w[i]),end='')
else:
    print("<%d>"%(w[0]))
    

 