import sys
input = sys.stdin.readline

def main():
    a, b = map(int, input().split())
    n, m = map(int, input().split())
    
    robot = [[0, 0, 0]]
    for _ in range(n):
        x, y, d = input().split()
        robot.append([int(x), int(y), "NESW".index(d)])
    
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    for _ in range(m):
        num, op, t = input().split()
        num, t = int(num), int(t)
        
        x, y, d = robot[num]
        if op == "F":
            nx, ny = x+dx[d]*t, y+dy[d]*t
            
            crashed_robot, dif = 0, 101
            for i in range(1, n+1):
                if i == num:
                    continue
                
                cx, cy, _ = robot[i]
                if d%2 == 1 and y == cy and abs(cx-x) < dif and \
                    (x < cx <= nx or nx <= cx < x):
                    crashed_robot = i
                    dif = abs(cx-x)
                elif d%2 == 0 and x == cx and abs(cy-y) < dif and \
                    (y < cy <= ny or ny <= cy < y):
                    crashed_robot = i
                    dif = abs(cy-y)
                    
            if crashed_robot:
                print(f"Robot {num} crashes into robot {crashed_robot}")
                exit()
            
            if not (0 < nx <= a and 0 < ny <= b):
                print(f"Robot {num} crashes into the wall")
                exit()
            
            robot[num] = [nx, ny, d]
        else:
            nd = (d + "_R_L".index(op)*t) % 4
            robot[num] = [x, y, nd]
    print("OK")
    
if __name__ == "__main__":
    main()