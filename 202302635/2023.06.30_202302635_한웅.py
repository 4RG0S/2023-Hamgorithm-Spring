from collections import deque
T = int(input())

c = [1 , -1 , 0 , 0] # 상하좌우 확인 리스트
c2 = [0 , 0 , 1 , -1]

def bachu(zm , X , Y) :      # bfs 이용
    q = deque()
    q.append((X , Y))
    zm[X][Y] = -1           

    while q :
        X , Y = q.popleft()
        for i in range(4) :
            XP = X + c[i]
            YP = Y + c2[i]
            if (0 <= XP < N) and (0 <= YP < M) :
                if zm[XP][YP] == 1 :
                    zm[XP][YP] = -1
                    q.append((XP,YP))      #배추가 있는 곳은 모두 -1로 변경
    

for i in range(T) :
    M , N , K = map(int,input().split())
    zm = [[0]*M for i in range(N)]
    cnt = 0

    for j in range(K) :
        X , Y = map(int,input().split())
        zm[Y][X] = 1

    for j in range(N) :
        for k in range(M) :
            if zm[j][k] == 1 : 
                bachu(zm, j, k)
                cnt += 1
    print(cnt)

