import sys

def main():
  n = int(sys.stdin.readline())
  xs = list(map(int, sys.stdin.readline().split()))
  xss = sorted(set(xs)) # sorted 정렬 O(n*log(n))
  xd = {x : i for i, x in enumerate(xss)} # 딕셔너리 사용
  xz = [xd[x] for x in xs] # 원래 입력받은 좌표에 맞게 압축된 값 할당
  print(*xz)
  
if __name__ == '__main__':
  main()

# 정렬하면 x좌표에 해당하는 인덱스 값 = 압축되는 값
# 이분탐색 안씀
