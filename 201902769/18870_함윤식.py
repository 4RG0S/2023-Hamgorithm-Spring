n = int(input())

arr = list(map(int, input().split()))
arr2 = sorted(list(set(arr)))

m = {}
for i in range(len(arr2)):
    m[arr2[i]] = i

for i in arr:
    print(m[i], end = ' ')