x=int(input())
y=[0]*x
for k in range(x):
    y[k]=input()
    y[k]=y[k].lower()
for i in range(x):
    print(y[i])
