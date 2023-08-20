import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    dic = {} # 입력 받은 옷 종류

    for i in range(n):
        a, b = input().split()

        # 해당 옷 종류가 이미 존재 할 경우 경우의 수 추가
        if b in dic:
            dic[b] += 1
        
        # 없으면 입고, 안입고의 두가지 경우이므로 2를 저장
        else:
            dic[b] = 2

    # 경우의 수(곱하기 위해 1로 저장)
    A = 1

    for j in dic:
        # 입력 받은 경우의 수 곱하기
        B = dic[j]
        A = A*B

    # 아무것도 안입는 경우 1가지를 제외하고 출력
    print(A-1)