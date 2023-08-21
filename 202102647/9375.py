import sys

input = sys.stdin.readline
testcase = int(input())
for _ in range(testcase):
    a = int(input())
    cloth = {}
    for i in range(a):
        name, kind = input().split()
        # 같은 종류의 옷이면 1을 +하고, 같은 종류의 옷이 없다면 새로 1을 생성
        if kind not in cloth:
            cloth[kind] = 1
        else:
            cloth[kind] += 1
    sum = 1

    for result in cloth.values():
        sum *= result + 1
    print(sum - 1)
