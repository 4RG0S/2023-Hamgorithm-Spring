import sys
input = sys.stdin.readline

N , M = map(int,input().split())
dic = {} # 포켓몬이 키, 번호가 값
dic2 = {} #번호가 키, 포켓몬이 값
for i in range(N) :
    pkm = input().rstrip()
    dic[pkm] = (i+1)
    dic2[i+1] = pkm

for i in range(M) :
    q = input().rstrip()
    if q.isnumeric() == False : #포켓몬의 번호를 물어봤을 경우
        print(dic[q]) #번호 출력
    else :  #반대의 경우
        print(dic2[int(q)]) #포켓몬 출력