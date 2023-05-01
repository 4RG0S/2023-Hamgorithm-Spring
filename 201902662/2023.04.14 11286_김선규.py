import heapq
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    h = []
    for _ in range(n):
        x = int(input())
        if x:
            heapq.heappush(h, (abs(x), x))
        else:
            try: 
                print(heapq.heappop(h)[1])
            except:
                print(0)
    
if __name__ == '__main__':
    main()