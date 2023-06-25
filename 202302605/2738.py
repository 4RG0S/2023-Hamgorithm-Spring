n, m = map(int, input().split())

arr1 = [[] for i in range(n)]
arr2 = [[] for i in range(n)]
arr3 = [[] for i in range(n)]

for j in range(n):
    arr1[j] = list(map(int, input().split()))

for k in range(n):
    arr2[k] = list(map(int, input().split()))

for a in range(n):
    for b in range(m):
        arr3[a].append(arr1[a][b] + arr2[a][b])

for a in range(n):
    for b in range(m):
        print(arr3[a][b], end = ' ')
    print()