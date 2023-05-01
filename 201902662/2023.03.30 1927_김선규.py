import heapq
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    heap = []
    for _ in range(n):
        x = int(input())
        if x:
            heapq.heappush(heap, x)
        else:
            if heap:
                print(heapq.heappop(heap))
            else:
                print(0)
    
if __name__ == '__main__':
    main()