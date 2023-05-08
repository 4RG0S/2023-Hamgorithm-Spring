t = int(input())

for _ in range(t):
    floor = int(input())
    num = int(input())
    f = [i for i in range(1, num+1)]
    for k in range(floor):  # 층 수 만큼 반복
        for i in range(1, num):  # 1 ~ n-1까지 (인덱스로 사용)
            f[i] += f[i-1]  # 층별 각 호실의 사람 수를 변경
    print(f[-1])