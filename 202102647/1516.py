import sys
from collections import deque

test = int(sys.stdin.readline())
degree = [0] * (test+1)
graph = [[] for _ in range (test+1)]
time = [0] * (test+1)
for i in range (1,test+1):
    data = list(map(int,sys.stdin.readline().split()))
    time[i] = data[0]
    building = data[1:len(data)-1]
    for j in building:
        graph[j].append(i)
        degree[i] += 1
        #차수 연결

#위상 정렬 시작
def topology_sort():
    result = [0] * (test+1)
    queue = deque()
    # 연결된게 애초에 없던 인자는 deque에 넣음
    for i in range (1,test+1):
        if degree[i] ==0:
            queue.append(i)
    # queue에 아무것도 없을 때까지 반복
    while queue:
        # queue의 첫번째 인자를 꺼냄
        target = queue.popleft()
        # 해당 타겟의 시간을 result에 더함
        result[target] += time[target]
        # target과 연결된 인자 확인
        for j in graph[target]:
            # 연결 인자와 끊음
            degree[j] -= 1
            # result 에 result[j]와 result[target] 중 시간이 큰 것을 더한다
            result[j] = max(result[j],result[target])
            # 연결이 다끊어지면 j를 queue에 넣음
            if degree[j] ==  0:
                queue.append(j)
    return result
r = topology_sort()
for i in range (1,test+1):
    print(r[i])