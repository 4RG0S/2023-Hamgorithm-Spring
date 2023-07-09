import heapq
import sys

hq = []
n = int(sys.stdin.readline())
for _ in range(n): # 입력을 heaq에 넣어주기
    ip = int(sys.stdin.readline())
    heapq.heappush(hq, ip)

if n ==1: # 만약 입력이 한 개면 비교 숫자랄 게 없음.
    print(0) # 비교 x
else: # 두 개 이상 존재할 경우
    sum = 0 # 누적으로 더해야 하니 sum 변수 초기화
    for value in range(n-1): # 두 개 씩 뽑을거니 n-1번 반복
        first = heapq.heappop(hq)
        seconde = heapq.heappop(hq) # 두 개를 뽑아서
        sum += first+seconde # 더한 값을 누적합
        heapq.heappush(hq, first+seconde) # 이 값을 다시 더해야 하니 넣어줌
    print(sum) # 계산 결과