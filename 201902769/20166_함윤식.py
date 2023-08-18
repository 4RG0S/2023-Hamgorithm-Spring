import collections
n,m,k = map(int, input().split())
data = []
pavorite = collections.defaultdict(list)
pavorite_list = []

for i in range(n):
    data.append([i for i in input()])

for i in range(k):
    pavorite_str = input()
    pavorite_list.append(pavorite_str)
    pavorite[pavorite_str] = 0

def search(x,y,s):
    if s in pavorite.keys():
        pavorite[s] += 1

    if len(s) == 5:
        return
    
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)]:
        word = data[(x+dx)%n][(y+dy)%m]
        search((x+dx)%n, (y+dy)%m, s + word)

for i in range(n):
    for j in range(m):
        search(i,j,data[i][j])

for i in pavorite_list:
    print(pavorite[i])

# 재귀로 문자열의 길이가 5가 될때까지 재귀를 돌린다.
# 8방위로 이동하면서 문자열을 더해준다.
# 재귀문제라 재밌었다.