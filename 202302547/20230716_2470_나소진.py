import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

start, end = 0, n-1
ans = arr[start] + arr[end] # 초기값 설정
idx = [arr[start], arr[end]] # ans의 각 배열 index를 저장

while start < end :
  sum = arr[start] + arr[end]
  if abs(sum) < ans : # 절대값이 가장 작은 경우를 저장
    ans = abs(sum)
    idx = [arr[start], arr[end]]
    if(ans == 0) : # 특성값이 0에 일치하면 연산 중단
      break
  if sum < 0 : # 합이 음수면 시작점 증가(양수에 가까워지게)
    start += 1
  else : # 합이 양수면 끝점 감소(음수에 가까워지게)
    end -= 1
  
print(idx[0], idx[1])

# 미해결 문제...