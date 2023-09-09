import sys

def main():
    # 두 톱니바퀴에 맞닿은 부분의 극이 같은지 확인하는 함수
    def check(wheel_a, wheel_b):
        if wheel_a[2] == wheel_b[6]: # 같으면 가만히
            return False
        else: # 다르면 회전
            return True
    # 톱니 바퀴를 방향에 맞게 회전시키는 함수
    def rotate(wheel, direction):
        if direction == 1: # 시계 방향
            wheel.insert(0, wheel.pop())
        elif direction == -1: # 반시계 방향
            wheel.append(wheel.pop(0))
        return wheel
    
    # i -> 0: 12시 ~ 7: 10시 30분
    # wheel[i] -> 0: N극, 1: S극
    wheel_1 = list(map(int, sys.stdin.readline().strip()))
    wheel_2 = list(map(int, sys.stdin.readline().strip()))
    wheel_3 = list(map(int, sys.stdin.readline().strip()))
    wheel_4 = list(map(int, sys.stdin.readline().strip()))
    
    K = int(sys.stdin.readline())
    # 톱니바퀴 돌리기
    for _ in range(K):
        between_12 = check(wheel_1, wheel_2)
        between_23 = check(wheel_2, wheel_3)
        between_34 = check(wheel_3, wheel_4)
        # a -> 톱니바퀴 번호, b -> 회전방향 (1: 시계, -1: 반시계) 
        a, b = map(int, sys.stdin.readline().split())

        if a == 1:
            wheel_1 = rotate(wheel_1, b)
            if between_12:
                wheel_2 = rotate(wheel_2, -b)
                if between_23:
                    wheel_3 = rotate(wheel_3, b)
                    if between_34:
                        wheel_4 = rotate(wheel_4, -b)
        elif a == 2:
            wheel_2 = rotate(wheel_2, b)
            if between_12:
                wheel_1 = rotate(wheel_1, -b)
            if between_23:
                wheel_3 = rotate(wheel_3, -b)
                if between_34:
                    wheel_4 = rotate(wheel_4, b)
        
        elif a == 3:
            wheel_3 = rotate(wheel_3, b)
            if between_23:
                wheel_2 = rotate(wheel_2, -b)
                if between_12:
                    wheel_1 = rotate(wheel_1, b)
            if between_34:
                wheel_4 = rotate(wheel_4, -b)
                
        elif a == 4:
            wheel_4 = rotate(wheel_4, b)
            if between_34:
                wheel_3 = rotate(wheel_3, -b)
                if between_23:
                    wheel_2 = rotate(wheel_2, b)
                    if between_12:
                        wheel_1 = rotate(wheel_1, -b)
   
    print(wheel_1[0] * 1 + wheel_2[0] * 2 + wheel_3[0] * 4 + wheel_4[0] * 8)          

if __name__ == "__main__":
    main()
