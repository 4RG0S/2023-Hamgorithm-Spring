x=int(input())
y=[0]*x
for k in range(x):
    y[k]=int(input())

y.sort()

for k in range(x):
    print(y[k])