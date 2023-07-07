# 1
# 메모리 초과
# 모든 수를 hq에 넣고 n번째 큰 수가 제일 작을 때까지 pop해서 출력했음
# import heapq
# import sys
# input = sys.stdin.readline
# n = int(input())
# hq = []
# for _ in range(n) :
#     x = list(map(int, input().split()))
#     for i in x :
#         heapq.heappush(hq, i)
# for _ in range(len(hq) - n) :
#     heapq.heappop(hq)
# print(hq[0])

# 2
# 메모리 초과
# 모든 수를 hq에 넣고 정렬 후 n번째 큰 수 출력
# import sys
# input = sys.stdin.readline
# n = int(input())
# hq = []
# for _ in range(n) :
#     x = list(map(int, input().split()))
#     for i in x :
#         hq.append(i)
# hq.sort()
# print(hq[-n])

# 3
# 모든 수를 저장하면 메모리 초과가 뜸
# N번 째 큰 수를 찾는 것이므로 hq의 원소가 N개보다 많을 필요가 없음
# hq의 크기를 N으로 제한해서 메모리 초과 해결 
# 1708ms 소요, 메모리 33324KB 사용
import heapq
import sys
input = sys.stdin.readline
n = int(input())
hq = []
for _ in range(n) :
    x = list(map(int, input().split()))
    for i in x :
        heapq.heappush(hq, i)
        if len(hq) > n : # hq의 원소 개수가 n이 넘어가면 
            heapq.heappop(hq) # hq의 가장 작은 원소 제거
# hq의 크기가 n을 넘어가면 가장 작은 원소를 제거했기 때문에
# hq에 남아있는 원소 중 가장 작은 값이 n번째로 큰 수이다.
print(hq[0])

# 4
# 구글 답안
# 3과 다른 점은 새로 들어오는 입력이 heap의 최소값보다 작으면 추가하지 않고 무시
# 1060ms 소요, 메모리 33324KB 사용
# 조건에 따라 append와 pop을 안하는 경우가 생기므로 시간이 줄어듦
# import heapq
# heap = []
# n = int(input())
# for _ in range(n):
#     numbers = map(int, input().split())
#     for number in numbers:
#         if len(heap) < n: # heap의 크기를 n개로 유지
#             heapq.heappush(heap, number)
#         else:
#             if heap[0] < number:
#                 heapq.heappop(heap)
#                 heapq.heappush(heap, number)
# print(heap[0])

# 5
# heapq 사용하지 않고 리스트만로는 해결할 수 없는지
# 각각의 입력을 하나씩 append하고 pop해서 시간초과
# import sys
# input = sys.stdin.readline
# n = int(input())
# hq = []
# for _ in range(n) :
#     x = list(map(int, input().split()))
#     for i in x :
#         hq.append(i)
#         hq.sort(reverse=True)
#         if len(hq) > n :
#             hq.pop()        
# print(hq[-1])

# 6
# 구글 답안
# 각 입력들을 하나씩 추가하는게 아닌 통째로 추가
# 인덱싱으로 원소 개수가 n개가 되도록 유지
# 816ms가 소요, 메모리 31256KB 사용
# import sys
# input = sys.stdin.readline
# n = int(input())
# arr = []
# for _ in range(n):
#     arr += list(map(int,input().split()))
#     arr = sorted(arr,reverse=True)[:n]
# print(arr[-1])

# 7
# 5에서 했던 코드 6기반으로 수정
# import sys
# input = sys.stdin.readline
# n = int(input())
# hq = []
# for _ in range(n) :
#     hq += list(map(int, input().split()))
#     hq.sort(reverse=True)
#     hq = hq[:n]
# print(hq[-1])

# heapq를 사용하면 입력을 일일이 최소 힙의 형태로 append하고 pop하기 때문에 시간, 메모리가 더 많이 필요
# list를 사용하면 각 행을 통째로 list에 추가하고 인덱싱으로 한 번에 자를 수 있어서 시간, 메모리를 더 적게 쓰는 것 같다.