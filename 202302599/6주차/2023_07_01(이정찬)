import sys

sys.setrecursionlimit(10000) # 재귀 오류 해결, 재귀 깊이 조정

yunsik = int(input())

def sexy_yunsik(a,b) : # dfs 활용
    B[a][b] = -1 # 재귀 단계에서 다시 한번 1이라 확인되면 안되니 변경 

    for i in [-1,1] :
        if a == 0 and i == -1 : # 리스트내에서 음수는 오버플로우 되어 최대 양수로 넘어감, 이를 조정
            continue
        q = a+i
        if q >= A[0] : # 리스트 내 크기 초과를 해결
            continue
        if B[q][b] == 1 :
            sexy_yunsik(q,b)
            
    for i in [-1,1] :
        if b == 0 and i == -1 :
            continue
        q = b+i
        if q >= A[1] :
            continue
        if B[a][q] == 1 :
            sexy_yunsik(a,q)

for i in range(yunsik) :
    B = []
    C = []
    A = list(map(int,input().split()))
    B = [[0 for j in range(A[1])]for i in range(A[0])] # 입력받은 크기 만큼 리스트 생성

    for j in range(A[2]) :
        a,b = map(int,input().split())
        B[a][b] = 1
        C.append([a,b]) # 리스트를 전부 돌며 1을 각각 확인 하면 오래 걸리니, 리스트 내에서 1로 입력받은 위치를 저장해놓음

    result = 0

    for j in C :
        if B[j[0]][j[1]] == 1 :
            sexy_yunsik(j[0],j[1])
            result += 1 

    print(result)