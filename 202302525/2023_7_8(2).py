#여름방학 '햄'고리즘 2주차(2)

import heapq
import sys

heap = []
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    num = int(input()) 

    if num == 0: # 입력이 0으로 주어질 경우, 가장 큰 수를 출력한다.
        try: #배열이 빈 경우를 고려하여, try-except문으로 작성한다.
            print(-heapq.heappop(heap)) 
        
        except:
            print(0) #배열이 빈 경우 0 출력

    else:
        heapq.heappush(heap, -num)