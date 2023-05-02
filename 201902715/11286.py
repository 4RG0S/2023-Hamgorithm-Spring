import sys
from heapq import heappush, heappop
from typing import Tuple, List


def push(heap: List[Tuple[int, int]], x: int) -> List[Tuple[int, int]]:
    """
    x를 heap에 넣어야 한다.
    출력할 때는 절뎃값을 출력해야 한다.
        절댓값이 가장 작은 값을 우선 출력한다.
        여러개라면, 가장 작은 수를 출력해야 한다. (음수를 먼저)
        그냥 (절댓값, 원래수) 이렇게 저장해버리면 될듯?
    """
    heappush(heap, (abs(x), x))
    return heap


def pop(heap: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    if len(heap) == 0:
        print(0)
        return heap
    print(heappop(heap)[1])
    return heap


def read_and_do(heap: List[Tuple[int, int]]):
    x = int(sys.stdin.readline())
    if x == 0:
        heap = pop(heap)
    else:
        heap = push(heap, x)
    return heap


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    heap = []
    [read_and_do(heap) for _ in range(n)]
