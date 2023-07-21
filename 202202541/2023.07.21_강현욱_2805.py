import sys
input=sys.stdin.readline
x,y=map(int,input().split())
ls=[]
ls=list(map(int,input().split()))
sum=0
top=max(ls)
bottom=0
po=len(ls)
ans=0
#ÀÌÁøÅ½»ö
while bottom<=top:
    mid=(bottom+top)//2
    for i in range(po):
        if (ls[i]-mid)>=0:
            sum=sum+(ls[i]-mid)
#ÃÖ´ñ°ª ¼±ÅÃ
    if sum>=y:
        if(mid>=ans):
            ans=mid
        bottom=mid+1
    else:
        top=mid-1
    sum=0
print(ans)
