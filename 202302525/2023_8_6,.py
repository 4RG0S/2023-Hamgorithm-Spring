import sys
input = sys.stdin.readline

def find(arg):
    if parent[arg] != arg: #자기자신이 조상노드가 아니라면
        parent[arg] = find(parent[arg]) #재귀를 이용하의 부모의 부모의... 조상을 찾는다

    return parent[arg] #조상노드를 반환

def union(arg1, arg2):
    x = find(arg1)
    y = find(arg2)

    if x != y: #x와 y가 같은 조상노드가 아니라면
        parent[x] = y #조상 바꿔치기
        groupsize[y] += groupsize[x] # UNION

    print(groupsize[y])
    # print(groupsize[f1])

testcase = int(input())

for _ in range(testcase):
    parent = {} 
    groupsize = {}

    f = int(input())
    
    for i in range(f):
        f1, f2 = input().split()

        if f1 not in parent:
            parent[f1] = f1
            groupsize[f1] = 1

        if f2 not in parent:
            parent[f2] = f2
            groupsize[f2] = 1

        union(f1, f2)

        # print(groupsize[f1])
        # print(groupsize[f2])