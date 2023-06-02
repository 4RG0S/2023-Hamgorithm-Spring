import sys
input = sys.stdin.readline

a, b = map(int, input().split())
a_lst = set(list(map(int, input().split())))
b_lst = set(list(map(int, input().split())))
cnt = 0
for i in a_lst :
    if i not in b_lst :
        cnt += 1
for j in b_lst :
    if j not in a_lst :
        cnt += 1
print(cnt)