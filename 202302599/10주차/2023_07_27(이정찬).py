from collections import deque
import sys

N,M = map(int,input().split())

indegree = [0] * N # 진입 차수 저장할 리스트
nod_infor = [[] for _ in range(N)] # 노드 간 연결을 확인할 리스트

height_infor = [] # 키 순서를 받아놓을 리스트
result = []

for i in range(M) :
    height_infor.append(list(map(int,input().split())))
    
for i in range(M) :    
    indegree[height_infor[i][1]-1] += 1 # 입력받은 키 정보에서 두번째 인자만 진입 차수를 +1함
    nod_infor[height_infor[i][0]-1].append(height_infor[i][1]) # 노드 정보 0번째 인덱스에 연결돼 있는 다른 노드 정보를 넣음

q = deque()

for i in range(N) :
    if indegree[i] == 0 :
        q.append(i+1) # 진입 차수 0인 원소를 삽입

while q : # 진입 차수 0인 원소와 인접한 다른 원소 진입 차수를 1씩 낮추며 큐에 새롭게 채워넣음.
    temp = q.popleft()
    result.append(temp)
    
    for i in nod_infor[temp-1] :
        indegree[i-1] -= 1

        if indegree[i-1] == 0 :
            q.append(i)

print(*result)