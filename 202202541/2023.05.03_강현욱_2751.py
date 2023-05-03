x=int(input())
y=x*[0]
for k in range(x):
    y[k]=int(input())
y.sort(reverse=False)
for k in range(x):
    print(y[k])