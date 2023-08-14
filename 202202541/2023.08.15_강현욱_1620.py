import sys
input=sys.stdin.readline
x,y=map(int,input().split())
dic={}
for i in range(1,x+1):
    name=input().rstrip()
    j=i
    j=str(i)
    dic[name]=j
    dic[j]=name
for j in range(y):
    qu=input().rstrip()
    print(dic[qu])
    