import heapq
import sys

N = int(sys.stdin.readline())

heap = []

for _ in range(N) :

    A = list(map(int,input().split())) 

    for i in A :
        heapq.heappush(heap, i) # 힙을 이용해서 원소를 밀어 넣음.

        if len(heap) > N :
            heapq.heappop(heap) # N번째 큰 수를 구하기 위해 힙의 길이가 N을 넘어가면 최소 원소를 지움.
                                # 큰 수들은 힙의 뒤쪽에 채워지니 N번째 큰 수보다 작은 수들만 사라짐.
print(heap[0])          