from sys import stdin

n, m = map(int, stdin.readline().rstrip().split())
by_id = {}
by_name = {}

for i in range(1, n + 1):
    pokemon = stdin.readline().rstrip()
    by_id[i] = pokemon
    by_name[pokemon] = i

for _ in range(m):
    x = stdin.readline().rstrip()
    if x.isdigit():
        print(by_id[int(x)])
    else:
        print(by_name[x])