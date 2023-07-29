import sys

input = sys.stdin.readline

# 업무의 수
task_count = int(input())

# 각 업무별로 얻을 수 있는 최대 이익을 저장하는 리스트
max_profit = [0] * (task_count + 1)

for i in range(1, task_count + 1):
    # 각 업무에 대한 정보 입력 받기 (이익 및 선행 업무)
    task_info = list(map(int, input().split()))

    # 선행 업무를 확인하면서 최대 이익 계산
    for prior_task in task_info[1:]:
        max_profit[i] = max(max_profit[i], max_profit[prior_task] + task_info[0])

# 전체 업무 중 최대 이익 출력
print(max(max_profit))
