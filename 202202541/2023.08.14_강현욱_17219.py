import sys
input=sys.stdin.readline
dic={}
x,y=map(int,input().split())
for j in range(x):
    site, pw=input().split()
    dic[site]=pw
for y in range(y):
    psw=input().rstrip()
    print(dic[psw])
