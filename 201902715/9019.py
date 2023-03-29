import sys
from collections import deque


MAX_NUM = 10000


def solve(a: int, b: int):
    return a_to_b(a, b)


def a_to_b(a: int, b: int):
    """정수 a로 정수 b를 만드는 데 필요한 최소 연산의 리스트를 문자열 형태로 반환"""

    bfs_tracking_arr = deque()
    bfs_tracking_arr.append((a, ""))

    visited = set()
    
    while True:
        a, command = bfs_tracking_arr.popleft()
        
        if a == b:
            return command

        temp = operation_d(a)
        if temp not in visited:
            visited.add(temp)
            bfs_tracking_arr.append((temp, command + "D"))

        temp = operation_s(a)
        if temp not in visited:
            visited.add(temp)
            bfs_tracking_arr.append((temp, command + "S"))

        temp = operation_l(a)
        if temp not in visited:
            visited.add(temp)
            bfs_tracking_arr.append((temp, command + "L"))

        temp = operation_r(a)
        if temp not in visited:
            visited.add(temp)
            bfs_tracking_arr.append((temp, command + "R"))


def operation_d(n: int):
    return (2 * n) % MAX_NUM


def operation_s(n: int):
    return (n - 1) % MAX_NUM


def operation_l(n: int):
    n_seq = list("0000" + str(n))[-4:]
    n_seq.append(n_seq[0])
    n_seq[0] = "0"
    return int("".join(n_seq))


def operation_r(n: int):
    n_seq = list("0000" + str(n))[-4:]
    n_seq.insert(0, n_seq.pop())
    return int("".join(n_seq))


def test_d():
    assert operation_d(500) == 1000
    assert operation_d(6000) == 2000


def test_s():
    assert operation_s(1000) == 999
    assert operation_s(0) == 9999


def test_l():
    assert operation_l(1234) == 2341
    assert operation_l(123) == 1230


def test_r():
    assert operation_r(1234) == 4123
    assert operation_r(1230) == 123
    assert operation_r(123) == 3012


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        A, B = map(int, sys.stdin.readline().split())
        print(solve(A, B))
