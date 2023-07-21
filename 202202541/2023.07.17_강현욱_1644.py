
import sys
input=sys.stdin.readline
x=int(input())
ls=[True]*4000001
prime=[]
#에스라토스네스의 체
for u in range(2,2001):
    if ls[u] == True:
        for j in range(u*2,4000001,u):
            ls[j]=False

for q in range(2, 4000001):
        if ls[q]:
            prime.append(q)
end=0
sum=0
key=0
n=0
k=0
while k<len(prime):
    if(prime[k]>x):
        n=k
        break
    elif(prime[k]==x):
        n=k+1
        break
    elif(x>prime[len(prime)-1]):
        n=len(prime)
        break
    k=k+1
#투포인터       
for start in range(n):
    while sum<x and end<n:
        sum+=prime[end]
        end+=1
    if(sum==x):
         key+=1
    sum-=prime[start]
if(x==1):
    print(0)
elif(x==2):
    print(1)
else:
    print(key)



        
