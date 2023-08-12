import sys

N,M = map(int,input().split())

parent = [i for i in range(N+1)] # 노드 간 연결을 확인해줄 배열

def find_nod(node) : # 상위 노드를 찾는 함수
    while parent[node] != node :
        parent[node] = parent[parent[node]] # 경로 압축
        node = parent[node]
    return node

for _ in range(M) :
    union = list(map(int,sys.stdin.readline().split()))

    if union[0] == 0 :
        if union[1] < union[2] : # 노드 연결이 꼬이면 안되기에 정렬 후에 사용
            temp_1 = union[1]
            temp_2 = union[2]
        else :
            temp_1 = union[2]
            temp_2 = union[1]
            
        parent[find_nod(temp_2)] = temp_1

    elif union[0] == 1 :
        temp_1 = union[1]
        temp_2 = union[2]

        temp_1 = find_nod(temp_1)
        temp_2 = find_nod(temp_2)

        if temp_1 == temp_2 :
            print("YES") 
        else :
            print("NO")