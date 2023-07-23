import sys, math

children, colors = map(int, sys.stdin.readline().split())
jewelry = []
for _ in range(colors):
    jewelry.append(int(sys.stdin.readline()))
start = 1
end = max(jewelry)

flat = sys.maxsize
# 이진탐색 시작
while start <= end:
    # 보석 최소 최대의 중간값 mid
    mid = (start + end) // 2
    temp = 0
    for i in jewelry:
        # temp에 jewelry / mid 를 더함
        temp += math.ceil(i / mid)
    if temp > children:  # temp가 학생수보다 크면 mid 오른쪽 부분으로
        start = mid + 1
    else:  # temp가 학생수보다 작으면 mid 왼쪽부분으로, mid값을 flat에 저장
        end = mid - 1
        flat = min(flat, mid)

print(flat)
