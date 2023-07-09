import heapq

def main():
    n, m = map(int, input().split())
    cards = list(map(int, input().split()))
    
    heap = []
    for c in cards:
        heapq.heappush(heap, c)
    
    # 우선순위 큐를 이용하여 가장 작은 두 수를 뽑아서 더한 후 다시 큐에 넣는다.
    for _ in range(m):
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        s = a + b
        heapq.heappush(heap, s)
        heapq.heappush(heap, s)

    print(sum(heap))
        
if __name__ == "__main__":
    main()