import sys
from collections import deque

N , M = map(int, sys.stdin.readline().split())

Ng = [[]for i in range(N + 1)] #노드 구현
Nc = [0] * (N + 1) #노드 연결을 카운트
q = deque()
r = []

for i in range(M) :
    A , B = map(int, sys.stdin.readline().split())
    Ng[A].append(B)
    Nc[B] += 1

for i in range(1, N + 1) :
    if Nc[i] == 0 : #만약 노드 연결 카운트가 0이라면
        q.append(i) #큐에 추가

while q : #노드 연결 카운트가 0이 될때까지 뺀 후 큐에 추가
    x = q.popleft()
    r.append(x)
    for i in Ng[x] :
        Nc[i] -= 1
        if Nc[i] == 0:
            q.append(i)

print(*r)