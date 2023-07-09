#여름방학 '햄'고리즘 2주차(3)

import sys
import heapq

heap = []
input = sys.stdin.readline

n = int(input())

def lenTest(arg:list) -> bool:
    '''
    heap의 크기를 제한한다.
    
    제한길이 초과 시 return False
    '''

    if len(arg) < n:
        return True
    
    else: 
        return False
    
    
for _ in range(n):
    nums = list(map(int, input().split()))

    for i in nums:
        if lenTest(heap):
            heapq.heappush(heap, i)

        else:
            heapq.heappush(heap, i)
            heapq.heappop(heap)

            #heapq 모듈(리스트)는 모든 원소들을 오름차순으로 정렬하는 것이 아님.
            #다만 tree의 root(0번째 인덱스)에는 가장 작은 수 가 오게 됨.
            #가장 나약한 자는 pop 할 수 있음 -> 최소한 리스트 내에서 가장 작은수만은 구할 수 있음(n번째 큰 수는 구할수 있다..!)

print(heapq.heappop(heap))
