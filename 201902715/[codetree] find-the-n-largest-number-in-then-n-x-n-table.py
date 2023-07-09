"""
b(i, j)의 원소들을 prior queue에 담아서 n번째로 큰 원소를 찾는다.

sequence를 입력받는 타이밍에 b(i, j)를 구할 수 있을까?
- i는 원소 입력받을 떄 index 이니 쉽게 알 수 있다.
- j는 1~n까지의 수를 넣으면 된다.
- int()로 소수점 버림을 진행한다.

=> naive하게 구현하니 메모리 초과 발생

prior queue의 크기를 n개만 유지할 수 있도록 바꾼다.
가장 큰 n개만 유지하고, 그 중 가장 작은 원소보다 큰 원소가 들어오면 그 때만 변경한다.

=> 시간 초과 발생

for loop으로 j를 1~n+1로 늘려가는 과정에서 문제가 있다고 판단.
a_i / 1 했을 때, prior queue에 들어갈 수 없다면, a_i / 2, a_i / 3, ... 또한 들어갈 수 없다는 게 자명하다.
따라서 break문을 추가해서 불필요한 연산을 하지 않도록 수정하여 해결했다.
"""


import sys
from typing import List
from heapq import heappush, heappop

n: int
prior_queue: List[int] = []

if __name__ == "__main__":
    n = int(sys.stdin.readline())

    for i, elem in enumerate(map(int, sys.stdin.readline().split())):
        for j in range(1, n + 1):
            element = int(elem / j)
            if len(prior_queue) < n:
                heappush(prior_queue, element)
            elif element > prior_queue[0]:
                heappop(prior_queue)
                heappush(prior_queue, element)
            else:
                break
    
    answer: int = prior_queue[0]
    
    print(answer)
