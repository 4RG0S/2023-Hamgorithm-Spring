import sys
input = sys.stdin.readline

def main():
    n, h = map(int, input().split())
    ss, jrs = [0 for _ in range(h)], [0 for _ in range(h)]
    for i in range(n):
        s = int(input())
        if i % 2:
            jrs[h-s] += 1
        else:
            ss[s-1] += 1
    
    for i in range(1, h):
        ss[h-i-1] = ss[h-i-1] + ss[h-i]
        jrs[i] = jrs[i] + jrs[i-1]

    cave = [0 for _ in range(h)]
    for i in range(h):
        cave[i] = ss[i] + jrs[i]
    
    m, cnt = min(cave), 0
    for i in cave:
        if i == m:
            cnt += 1
    print(m, cnt)
    
if __name__ == "__main__":
    main()