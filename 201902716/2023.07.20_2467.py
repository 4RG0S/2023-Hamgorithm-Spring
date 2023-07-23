import sys

def main():
  n = int(sys.stdin.readline())
  yong = list(map(int, sys.stdin.readline().split()))
  mixed = 2e9 # 0에 가까운 혼합용액 초기화
  l, r = 0, n-1
  y1, y2 = 0, 0
  ### 투 포인터 ###
  while l < r:
    cur_mixed = yong[l] + yong[r] # 혼합용액
    if mixed > abs(cur_mixed): # 현재 용액 절댓값과 비교
      y1, y2 = yong[l], yong[r] # 0에 가까운 혼합용액을 만드는 두 용액 갱신
      mixed = abs(cur_mixed) # 0에 가까운 혼합용액 갱신
      if mixed == 0: # 탈출
        break
    if cur_mixed <= 0: # 혼합용액이 0보다 작거나 같으면
      l += 1 # 왼쪽 포인터 한 칸 +
    else: # 혼합 용액이 0보다 크면
      r -= 1 # 오른쪽 포인터 한 칸 -
  print(y1, y2)

if __name__ == '__main__':
  main()

# 절댓값 이용, 0이 가장 작은 값
# 이분탐색 안씀
