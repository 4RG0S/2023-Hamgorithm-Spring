import sys

n,m = map(int,sys.stdin.readline().split())
pw = {}

for i in range(n):
    name, pwd = sys.stdin.readline().split()
    pw[name] = pwd

for _ in range(m):
    print(pw[sys.stdin.readline().rstrip()])
