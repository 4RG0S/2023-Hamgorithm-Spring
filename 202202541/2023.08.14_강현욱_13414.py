import sys
input=sys.stdin.readline
dic={}
dic2={}
x,y=map(int,input().split())
for k in range(y):
    num=input().rstrip()
    dic[num]=k
for k, v in dic.items():
    dic2[v]=k
ls=list(dic.values())
ls.sort()
if x<=len(ls):
    for j in range(x):
        print(dic2[ls[j]])
elif x>len(ls):
    for j in range(len(ls)):
        print(dic2[ls[j]])