import sys
import heapq 

def main():
    N = int(sys.stdin.readline()) 
    ham = list(map(int, sys.stdin.readline().split())) # 초기 햄 (첫번째 줄 원소 리스트)
    heapq.heapify(ham) # 최소 힙으로 만들기

    for _ in range(N-1):
        nham = list(map(int, sys.stdin.readline().split())) # 다음 햄 (N번째 줄 원소 리스트)
        for i in range(N):
            x = heapq.heappop(ham) # 햄에서 최솟값 pop
            
            if x < nham[i]: # 햄에 최솟값보다 큰 다음 햄에 값들은 push 
                heapq.heappush(ham, nham[i])
            else: # 아니면 햄에 최솟값 다시 push
                heapq.heappush(ham, x)
        
    print(ham[0]) # N번째 큰 수 == N크기 최소 힙의 root
    
if __name__ == '__main__':
    main()

# 원소 전체를 리스트로 받아서 구하면 메모리초과..
# N크기 리스트 이용
