import sys

hash = {}

num = int(sys.stdin.readline())
for _ in range(num):
    name, situation = map(str, sys.stdin.readline().split())
    if situation == 'leave':
        del hash[name]
    else:
        hash[name] = situation
re = sorted(hash.keys(), reverse=True)

for key in re:
    print(key)