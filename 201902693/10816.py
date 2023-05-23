import sys
from collections import Counter
input = sys.stdin.readline
a = int(input())
a_lst = list(map(int, input().split()))
b = int(input())
b_lst = list(map(int, input().split()))

cnt = Counter(a_lst)
result = []
for i in b_lst :
    if i in cnt :
        result.append(cnt[i])
    else :
        result.append(0)

print(*result)