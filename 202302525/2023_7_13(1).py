import sys
input = sys.stdin.readline
arr = []
s, e, = 0, 0
n, d, k, c = map(int, input().split())
sum = []
result = []

for _ in range(n):
    arr.append(int(input()))

for i in range(k-1):
    arr.append(arr[i])

for start in range(n):
    while len(sum) < k and e < len(arr):
        sum.append(arr[e])
        e += 1

    if len(sum) == k:
        sum_set = {x for x in sum} #중복제거를 위해 set으로 변환
        sum_set.add(c) #서비스 추가
        result.append(len(sum_set)) #초밥종류의 갯수를 추가

    del sum[0]

result.sort(reverse=True)
print(result[0])