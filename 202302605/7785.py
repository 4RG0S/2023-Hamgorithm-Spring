import sys

input = sys.stdin.readline

n = int(input())
dic = {} # 회사에 있는 사람 딕셔너리

for i in range(n):
    a, b = input().split()

    # 출입 시 딕셔너리에 저장
    if b == 'enter':
        dic[a] = b

    # 나가면 삭제
    else:
        del dic[a]

dic = sorted(dic.keys(), reverse=True)

for j in dic:
    print(j)