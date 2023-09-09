import sys
import collections
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n = int(input())

def lower_bound(arr, target):
    start, end = 0, len(arr)-1
    if target > arr[len(arr) - 1]:
        return len(arr)
    
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid
    return end

P = [int(input())]
h = collections.defaultdict(int)
result = 0
for i in range(1, n):
    print(P)
    cur = int(input())
    idx = lower_bound(P, cur)
    if idx == 0:
        height = h[P[0]] + 1
    elif idx == len(P):
        height = h[P[-1]] + 1
    else:
        height = max(h[P[idx]], h[P[idx-1]]) + 1
    P = set(P)
    P.add(cur)
    P = list(P)
    result += height

print(result + 1)
# 이진 탐색 트리를 시뮬레이션 하면 최악의 경우 n^2이 되어 시간초과가 발생한다.
# 시뮬레이션 하지 않고 풀어야 한다. lower_bound를 이용하여(log n) insert 위치를 찾는다.
# 높이의 경우 insert 위치의 좌, 우 노드중 최대값 + 1이 된다.
# insert시 복잡도가 O(n)이므로 최악의 경우 O(n^2)이 된다.
# 이를 해결하기 위해 set을 이용하려다가 안됨... 다음에 다시 도전함