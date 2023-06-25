import sys
input = sys.stdin.readline

n = int(input())

lst = [list(map(int, input().split(" "))) for _ in range(n)]
ans =[]

for i in range(n):
    cnt =0
    for j in range(n):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            cnt += 1
    ans.append(cnt+1)

for i in ans:
    print(i, end=" ")