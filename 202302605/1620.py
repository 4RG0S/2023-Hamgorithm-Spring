import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dic = {} # 입력 받은 포켓몬을 저장할 딕셔너리

for i in range(n):
    a = input().rstrip()

    # 입력 받은 포켓몬을 이름:번호 / 번호:이름 두 개로 저장
    dic[a] = i+1
    dic[str(i+1)] = a

for j in range(m):
    # 출력해야 할 포켓몬의 이름 혹은 번호를 입력 받고 출력
    b = input().rstrip()
    print(dic[b])