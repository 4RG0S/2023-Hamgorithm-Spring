
n,m = map(int, input().split())
group = {} # 그룹에 여러 멤버 들어가도록
mem_group = {} # 멤버당 해당되는 그룹 지정
for _ in range (n):
    groupname = input()
    groupsize = int(input())
    group[groupname]= [] # groupname이 key인 해시 생성
    for j in range (groupsize):
        name = input()
        group[groupname].append(name)
        mem_group[name] = groupname
for _ in range (m):
    name = input()
    gametype = int(input())
    # 1이면 팀이름, 0이면 멤버이름 사전순
    if gametype == 0: # 정렬 후 멤버 print
        for i in sorted(group[name]):
            print(i)
    else:
        print(mem_group[name])
