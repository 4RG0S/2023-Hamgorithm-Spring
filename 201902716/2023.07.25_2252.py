import sys
from collections import deque

def wesang_sort(edge, indegree):
    result = []
    queue = deque()

    for i in range(1, len(edge)):
        if indegree[i] == 0: # 정점에 진입차수가 0이면
            queue.append(i) # queue에 삽입
    
    while queue: # queue 정점 빌 때 까지 반복
        cur = queue.popleft() # 현재 정점
        result.append(cur) # 현재 정점을 결과 리스트에 삽입
        for next in edge[cur]: # 현재 정점과 연결된 정점들을 탐색
            indegree[next] -= 1 # 연결된 정점의 진입차수 -1
            if indegree[next] == 0: # 연결된 정점의 진입차수가 0이면
                queue.append(next) # 연결된 정점을 queue에 삽입
    return result

def main():
    ##### 입력 #####
    n, m = map(int, sys.stdin.readline().split()) # 학생 수, 비교 수
    comp = [[] for _ in range(n + 1)] # 비교 리스트
    indegree = [0] * (n + 1) # 진입차수 확인 리스트

    for _ in range(m): # 그래프 입력
        a, b = map(int, sys.stdin.readline().split()) # 작은 학생, 큰 학생
        comp[a].append(b)
        indegree[b] += 1 # 진입차수 +1
   
    ##### 출력 #####
    print(*wesang_sort(comp, indegree))

if __name__ == "__main__":
    main()
