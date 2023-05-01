x=[0]*5
sum=0
for k in range(5):
    x[k]=int(input())
    sum+=x[k]

x.sort()
print(int(sum/5))
print(x[2])
 