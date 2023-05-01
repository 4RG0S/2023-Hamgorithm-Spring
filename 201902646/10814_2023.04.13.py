from sys import stdin
T = int(stdin.readline())
user = []
for i in range(T):
    user.append(stdin.readline().split())
user.sort(key=lambda x:int(x[0]))
for info in user:
    print(" ".join(map(str, info)))
