import sys
input = sys.stdin.readline

lst = [list(map(int, input().split())) for _ in range(int(input()))]


lst.sort(key=lambda x: (x[1], x[0]))

for i in lst:
    print(*i)