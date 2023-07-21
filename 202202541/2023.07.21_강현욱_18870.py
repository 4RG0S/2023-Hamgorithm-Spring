import sys
input=sys.stdin.readline
x=int(input())
ls1=[]
ls1=list(map(int,input().split()))
ls=[]
#set 시간복잡도 1
ls=sorted(set(ls1))
#딕션너리 시간복잡도 1
my_dict = {value: index for index, value in enumerate(ls)}
for i in ls1:
    print("%d "%(my_dict[i]),end='')
