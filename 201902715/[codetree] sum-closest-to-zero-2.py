import sys
from typing import List


n: int
li: List[int]


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    li = list(map(int, sys.stdin.readline().split()))
    s, e = 0, n - 1
    acc = li[s] + li[e]
    result = (li[s], li[e])
    while s < e: # start 포인터는 end포인터보다 항상 작아야 한다.
        current = li[s] + li[e]
        if abs(current) < abs(acc): # 가장 0에 가까운 값을 구하기 위해
            acc = current
            result = (li[s], li[e])
        elif abs(current) == abs(acc): # 그 중, 더 작은 값이 최소인 쌍을 구하기 위해
            if li[s] < result[0]:
                result = (li[s], li[e])
        
        if current < 0:
            s += 1
        else:
            e -= 1
    
    print(result[0], result[1])
