import sys
input = sys.stdin.readline

n = input()

lst1 = list(map(int, input().split()))
lst2 = sorted(list(set(lst1)))
# lst2 = sorted()

d = {lst2[i]:i for i in range(len(lst2))}

for i in lst1:
    print(d[i], end=' ')
