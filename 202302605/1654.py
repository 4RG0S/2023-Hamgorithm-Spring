import sys

input = sys.stdin.readline

k, n = map(int, input().split())
arr = []

for i in range(k):
    arr.append(int(input()))

# 이분 탐색을 위한 시작과 끝 설정
start, end = 1, max(arr)

while end >= start:
    mid = (start + end) // 2
    sum = 0

    for i in arr:
        sum += i // mid

    # sum의 값이 n과 같거나 크면 start를, 작으면 end를 조절
    if sum >= n:
        start = mid + 1

    else:
        end = mid - 1

print(end)