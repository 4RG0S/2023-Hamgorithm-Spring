import heapq
# 최소 힙 사용을 위해 heapq import
# heapq는 최소 힙이기 때문에 최대 힙을 구현하기 위해
# 배열에 넣는 값을 음수로 바꿔서 넣어주면 최소 힙으로 최대 힙을 구현 가능
import sys
input = sys.stdin.readline

n = int(input())
hq = []
for _ in range(n) :
    x = int(input())
    if x == 0 : # 입력이 0일 때
        if len(hq) == 0 : # hq가 비어있으면
            print(0) # 0출력
        else : 
            print(-(heapq.heappop(hq))) # hq에서 가장 작은 값의 부호를 바꿔서 출력
    else :
        heapq.heappush(hq, -x) # hq에 입력을 음수로 바꿔서 추가