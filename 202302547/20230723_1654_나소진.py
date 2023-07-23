import sys

input = sys.stdin.readline
arr = []
k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

start, end = 1, max(arr)
len = 0  # 랜선의 길이 (결과값)

while start <= end:
  mid = (start + end) // 2  # 이진 탐색으로 랜선의 길이 연산
  sum = 0
  for i in arr:
    sum += i // mid  # 가능한 랜선의 개수 저장

  if sum >= n:  # 랜선의 개수가 필요한 개수거나 그보다 많으면 결과로 저장
    start = mid + 1
    len = mid
  else:  # 필요한 개수보다 적으면 end값을 조정하여 연산
    end = mid - 1

print(len)
