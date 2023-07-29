# 위상 정렬
import sys
from collections import deque

input = sys.stdin.readline

# 테스트 케이스의 수
test_count = int(input())

# 각 테스트 케이스에 대한 답을 저장할 리스트
answers = [0] * test_count

for t in range(test_count):
    n, k = map(int, input().split())

    # 각 건물을 짓는데 걸리는 시간
    build_times = [0] + list(map(int, input().split()))

    # 각 건물의 선행 건물 리스트와 진입 차수
    adj_list = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    for _ in range(k):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        indegree[b] += 1

    # 목표 건물 번호
    target_building = int(input())

    # 위상정렬을 사용하여 각 건물을 짓는데 필요한 최소 시간 계산
    result_times = [0] * (n + 1)
    queue = deque()

    # 진입 차수가 0인 건물들부터 시작
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
            result_times[i] = build_times[i]

    while queue:
        current_building = queue.popleft()
        if current_building == target_building:
            break

        for next_building in adj_list[current_building]:
            result_times[next_building] = max(result_times[next_building],
                                              result_times[current_building] + build_times[next_building])
            indegree[next_building] -= 1
            if indegree[next_building] == 0:
                queue.append(next_building)

    answers[t] = result_times[target_building]

for answer in answers:
    print(answer)
