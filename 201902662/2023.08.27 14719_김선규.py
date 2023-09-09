def main():
    h, w = map(int, input().split())
    bh = list(map(int, input().split()))
    
    world = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(w):
        for j in range(bh[i]):
            world[j][i] = 1
    
    cnt = 0
    for i in range(h):
        start = 0
        for j in range(w):
            if world[i][j] == 1:
                if start != 0:
                    cnt += j-start
                start = j+1
    print(cnt)
    
if __name__ == "__main__":
    main()