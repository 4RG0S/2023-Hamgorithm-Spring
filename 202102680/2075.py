import sys

n = int(input())
numbers = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = numbers[n-1]   # 맨 밑줄 배열 만 읽어옴
check = [n-1] * n   # 몇 번째 줄 까지 읽었는 지 확인
ans = -1000000000
# 맨 밑줄을 해당 열의 가장 큰 값으로 계속 갱신할 수 있도록 함
for _ in range(n):
    temp = result[0]    # 비교를 위한 초기값 설정
    ctrl_s = 0          # 어디까지 읽었나 저장
    for i in range(n):
        if result[i] > temp:    # 반복문 돌며 최댓값 찾기
            ctrl_s = i          # 최댓값이 몇 번째에 위치 했는 지 찾기 위해
            temp = result[i]    # 최댓값 저장
    ans = temp          # 최댓값
    check[ctrl_s] -= 1  # 한 칸 위의 수를 읽어와야 하므로 -1 해줌
    result[ctrl_s] = numbers[check[ctrl_s]][ctrl_s]     # 최댓값을 최댓값이 위치한 열에서 최댓값 바로 위에 위치한 수로 대체

print(ans)


