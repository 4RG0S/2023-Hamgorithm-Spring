import sys
input=sys.stdin.readline
x,y=map(int,input().split())
ls=[]
ls=list(map(int, input().split()))
start=0
end=0
sum=0
lth=[]
#투포인터 활용
for start in range(x):
    while sum<y and end<x:
        sum+=ls[end]
        end+=1
    if(sum>=y):
        lth.append(end-start)
        #길이 추가해서 작은거 출력
    sum=sum-ls[start]
lth.sort()
#해당하는게 없다면 lth 리스트 길이가 0임``
if(len(lth)==0):
    print(0)
else:
    print(lth[0])


