def union(x,y):
    x = find(x)
    y = find(y)
    if x < y:
        cities[y] = x
    else:
        cities[x] = y


def find(x):
    if x != cities[x]:
        cities[x] = find(cities[x])
    return cities[x]


n = int(input())
m = int(input())
cities = [i for i in range(n)]

for i in range(n):
    li = list(map(int,input().split()))
    for j in range(n):
        if li[j] == 1:  # 입력받은 거 돌면서 1이면 합치기
            union(i,j)

tour = list(map(int,input().split()))
start = cities[tour[0]-1]   # 시작 지점
for i in range(m):
    if cities[tour[i]-1] != start:  # 갈 수 있는 지 확인 후 불가면 NO 출력 후 break
        print("NO")
        break
else:
    print("YES")    # 중간에 break 가 없었다면 잘 수행된 것이므로 YES 출력