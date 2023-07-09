import heapq

# i를 순회하며 A[i-l+1] ~ A[i]사이의 수 중 최솟값을 찾는 문제
# heap에 값과 index 번호를 저장
# heap에서 최솟값을 pop하였을때 원소의 index가 
# 범위를 벗어나면 범위에 속하는 원소가 나올 때까지 pop
# 범위에 속하는 원소가 나오면 값을 정답에 저장 후 다시 heap에 저장
def main():
    n, l = map(int, input().split())
    li = list(map(int, input().split()))
    
    ans, heap = [], []
    for i in range(n):
        e, j = heapq.heappushpop(heap, (li[i], i))
        while i-l >= j:
            e, j = heapq.heappop(heap)
        heapq.heappush(heap, (e, j))
        ans.append(e)     
    print(*ans)
    
if __name__ == "__main__":
    main()