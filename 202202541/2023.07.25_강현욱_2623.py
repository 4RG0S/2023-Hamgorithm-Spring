from collections import deque
import sys
input=sys.stdin.readline
member, case=map(int,input().split())
member_case=[[] for i in range(member+1)]
link_case=[0]*(member+1)
result=[]
for k in range(case):
    ls=list(map(int, input().split()))
    for j in range(1,ls[0]):
        member_case[ls[j]].append(ls[j+1])
        link_case[ls[j+1]]+=1
    ls.clear()
q=deque()
for i in range(1,member+1):
    if link_case[i]==0:
        q.append(i)
while q:
    now=q.popleft()
    result.append(now)
    for i in member_case[now]:
        link_case[i]-=1
        if link_case[i]==0:
            q.append(i)
    if int(-1) in link_case:
        break
if len(result)!=member:
    print(0)
else:
    for z in range(0,len(result)):
        print(result[z])
