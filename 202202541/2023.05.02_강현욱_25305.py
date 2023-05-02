x=list(map(int,input().split()))
y=list(map(int,input().split()))
y.sort(reverse=True)
print(y[x[1]-1])