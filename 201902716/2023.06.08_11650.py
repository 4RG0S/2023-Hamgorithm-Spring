def main():
    N = int(input())
    points = []

    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    points.sort()
    
    for p in points:
        print(p[0], p[1])
                
if __name__ == '__main__':
    main()
