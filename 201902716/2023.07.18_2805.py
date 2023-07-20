import sys

def main():
  n, m = map(int, sys.stdin.readline().split())
  trees = list(map(int, sys.stdin.readline().split()))
  answer = 0
  l, r = 1, max(trees) # l, r 초기화
  ### 이분탐색 ###
  while l <= r: 
    mid = (l + r) // 2
    Sanggeun = 0
    # 상근이가 가져갈 나무 길이, 자르는 높이보다 낮은 나무는 0m 가져감
    for tree in trees:
      Sanggeun += (tree - mid) if tree > mid else 0
    if Sanggeun >= m: # 가져갈 나무길이가 m보다 크거나 같을 때
      l = mid + 1 # 왼쪽 인덱스 -> 중간 인덱스 + 1
      answer = mid # 정답 갱신
      if Sanggeun == m: # 탈출
        break
    else: # 가져갈 나무길이가 m보다 작을 때
      r = mid - 1 # 오른쪽 인덱스 -> 중간 인덱스 - 1
  print(answer)
  
if __name__ == '__main__':
    main()
