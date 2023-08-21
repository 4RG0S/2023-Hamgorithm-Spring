import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic, dic2 = {}, {} # 팀명저장 dic, 멤버이름 dic2

for _ in range(N):
    team = input().rstrip()
    member = []
    for i in range(int(input())):
        name = input().rstrip()
        dic[name] = team
        member.append(name)
    dic2[team] = member

for _ in range(M):
    mem = input().rstrip()
    quiz = int(input())
    if quiz == 1: # 팀 이름이 문제인 경우
        print(dic[mem])
    else: # 멤버 이름들이 문제인 경우
        ans = dic2[mem]
        ans.sort()
        for elem in ans:
            print(elem)
