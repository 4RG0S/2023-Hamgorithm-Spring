dic = {}

n = int(input())

for _ in range(n):
    name, state = input().split()
    dic[name] = state

for key in sorted(list(dic.keys()), reverse=True):
    if dic[key] == 'enter':
        print(key) 