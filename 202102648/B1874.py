import sys

n = int(input())
lst = [int(sys.stdin.readline()) for _ in range(n)]

s = []
ans = []
F = True
cnt = 0

for num in lst:
    while cnt < num:
        cnt += 1
        s.append(cnt)
        ans.append('+')
        
    if s[-1] == num:
        s.pop()
        ans.append('-')
    else:
        F = False
        break
    
if F == False:
    print("NO")
else:
    for i in range(len(ans)):
        print(ans[i])