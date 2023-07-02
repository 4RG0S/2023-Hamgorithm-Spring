A,B = map(int,input().split())
C = []

for i in range(A) :
    C.append(list(input()))

result = 0


def dfs(a,b) :
    if C[a][b] == "|" :
        C[a][b] = "yunsik" #확인된 노드를 다른 문자열로 변경
        for i in [1,-1] :
            temp_a = a+i # "|"에 대해서는 세로축 확인
            if (temp_a > 0 and temp_a < A) and C[temp_a][b] == "|" :
                dfs(temp_a,b) #문자열이 얼마나 반복되는지 재귀적으로 탐색

    if C[a][b] == "-" :
        C[a][b] = "yunsik" #확인된 노드를 다른 문자열로 변경
        for i in [1,-1] :
            temp_b = b+i # "-"에 대해서는 가로축 확인
            if (temp_b > 0 and temp_b < B) and C[a][temp_b] == "-" :
                dfs(a,temp_b) # 문자열이 얼마나 반복되는지 재귀적으로 탐색

for i in range(A) :
    for j in range(B) :
        if C[i][j] == "|" or C[i][j] == "-" : #필요한 문자에 대해서만 탐색
            dfs(i,j)
            result += 1

print(result)