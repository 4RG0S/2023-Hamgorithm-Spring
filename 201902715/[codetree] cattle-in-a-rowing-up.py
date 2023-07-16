import sys
from typing import List


N: int
position_of_cows: List[int] = []
x_i: int
y_i: int
z_i: int


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    for i in range(N):
        position = int(sys.stdin.readline())
        position_of_cows.append(position)
    
    # 우선 가장 쉬운 x < y < z를 만족하기 위해, 정렬합니다.
    position_of_cows = sorted(position_of_cows)

    # 문제의 조건을 잘 해석해보면
    # X___Y____Z (Y-X: x와 y의 거리 = a, Z-Y: y와 z의 거리 = b) 라고 했을 때,
    # a <= b <= 2 * a 라는 조건임

    # x는 고정시켜놓고, y z를 바꿔가며 찾고
    # 더이상 못 찾으면 x를 1증가시킨채로 다시 찾는다.
    
    result = 0

    x_i = 0
    y_i = 1
    z_i = 2
    while True:
        try:
            x, y, z = position_of_cows[x_i], position_of_cows[y_i], position_of_cows[z_i]
        except:
            x_i += 1
            y_i = x_i + 1
            z_i = y_i + 1
            if z_i >= len(position_of_cows):
                print(result)
                exit()
            continue
        dist_xy = y - x
        dist_yz = z - y
        if dist_xy > dist_yz:
            z_i += 1
            continue
        if dist_yz > 2 * dist_xy:
            y_i += 1
            z_i = y_i + 1
            continue
        
        result += 1
        if z_i == len(position_of_cows) - 1:
            y_i += 1
            z_i = y_i + 1
        else:
            z_i += 1
