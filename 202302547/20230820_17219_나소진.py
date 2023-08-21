import sys

input = sys.stdin.readline
dic = {}

n, m = map(int, input().split())

for i in range(n):
    name, pw = input().split()
    dic[name] = pw
    
for i in range(m):
    temp = input().strip()
    print(dic[temp])