def main():
    test_case = int(input())
    for _ in range(test_case):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        d = ((abs(x1-x2)**2 + abs(y1-y2)**2)**0.5)
        
        if d == 0 and r1 == r2:
            print(-1)
        elif d > r1 + r2 or d < abs(r1 - r2):
            print(0)
        elif d == r1 + r2 or d == abs(r1 - r2) :
            print(1)
        else:
            print(2)          
            
if __name__ == '__main__':
    main()
