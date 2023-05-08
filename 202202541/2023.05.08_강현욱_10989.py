import sys
n=int(input())
x=[0]*10001
for k in range(n):
    num=int(sys.stdin.readline())
    x[num]=x[num]+1
for i in range(10001):
    if(x[i]!=0):
        for u in range(x[i]):
            print(i)

