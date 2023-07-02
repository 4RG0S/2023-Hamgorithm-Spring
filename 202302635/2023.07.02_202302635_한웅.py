from collections import deque

M , N = map(int,input().split())


c = [1 , -1 , 0 , 0]    # 상하좌우 탐색 리스트
c2 = [0 , 0 , 1 , -1]   # 위와 같음
r = []                  # 토마토의 상태를 저장하는 리스트
cnt = 0                 
for i in range(N) :
    r.append(list(map(int,input().split())))
q = deque([])   

for i in range(N) :
    for j in range(M) :
        if r[i][j] == 1 :
            q.append([i,j])


def tomato() : #토마토 찾기
    
    
    while q :

        X , Y = q.popleft()

        for i in range(4) :
            XP = X + c[i]
            YP = Y + c2[i]
            if (0 <= XP < N) and (0 <= YP < M) :
                if r[XP][YP] == 0 :
                    r[XP][YP] = r[X][Y] + 1     
                    q.append([XP , YP])



tomato()

for i in r :
    for j in i :
        if j == 0:     
            print(-1)
            exit()


    
    cnt = max(cnt,max(i))

print(cnt-1)
print(r)

