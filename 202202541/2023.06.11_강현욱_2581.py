x=int(input())
y=int(input())
key=-2
z=[]
for k in range(x,y+1):
    key=-2
    for y in range(2,k):
        if(k%y==0):
            key=-3
            break
    if(key==-2):
        z.append(k)
sum=0
if(1 in z):
    del z[0]
if(len(z)!=0):
    for h in range(len(z)):
        sum+=z[h]
    print(sum)
    print(z[0])
else:
    print(-1)

       
