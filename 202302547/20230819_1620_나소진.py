import sys

input = sys.stdin.readline
dic = {}
dic2 = {}

n, m = map(int, input().split())

for i in range(n):
    name = input().strip()
    dic[name] = i + 1
    dic2[i+1] = name
    

for i in range(m):
    temp = input().strip()
    if temp in dic.keys():
        print(dic[temp])
    else:
        temp = int(temp)
        print(dic2[temp])