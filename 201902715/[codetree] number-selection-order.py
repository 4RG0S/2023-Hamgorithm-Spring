import sys
from typing import List, Tuple
from heapq import heappush, heappop
from collections import deque


N: int
X: int
numbers: List[int]
queue: deque
prior_queue: List[int]


if __name__ == "__main__":
    N, X = map(int, sys.stdin.readline().split())
    numbers = list(map(int, sys.stdin.readline().split()))
    queue = deque()
    prior_queue = []
    for i, elem in enumerate(numbers):
        heappush(prior_queue, -elem)
        queue.append((elem, i))
    
    # naive한 구현
    answer = 1
    while True:
        # prior queue에서 얻은 max원소가 나타날 때까지 추출 및 삽입 반복
        elem, i = queue.popleft()
        target = -heappop(prior_queue)
        while elem != target:
            if elem == target and i == X:
                print(answer)
                exit() # 종료 로직은 exit으로 대신함
            queue.append((elem, i))
            elem, i = queue.popleft()

        if elem == target and i == X:
            print(answer)
            exit() # 종료 로직은 exit으로 대신함
        answer += 1
