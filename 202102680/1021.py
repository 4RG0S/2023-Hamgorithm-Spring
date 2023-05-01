from collections import deque
from sys import stdin
n,m = map(int,stdin.readline().split())
num = deque()
l = list(map(int,stdin.readline().split()))
for i in range(n):
    num.append(i+1)

count = 0
temp1 = num.copy()
temp2 = num.copy()

i = 0
while i < len(l):
    if l[i] == temp1[0]:
        temp1.popleft()
        temp2 = temp1.copy()
        i += 1
    elif l[i] == temp2[0]:
        temp2.popleft()
        temp1 = temp2.copy()
        i += 1
    else:
        temp1.rotate(1)
        temp2.rotate(-1)
        count += 1


print(count)
