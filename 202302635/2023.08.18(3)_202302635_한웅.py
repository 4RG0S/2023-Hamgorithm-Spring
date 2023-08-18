import sys
input = sys.stdin.readline

t = int(input())

for i in range(t) :
    dic = {}
    n = int(input())
    for i in range(n) : 
        a , b = input().split()
        if dic.get(b) == None : #딕셔너리 안에 아직 같은 종류의 옷이 없으면
            dic[b] = set() #set함수 추가 후
        dic[b].add(a)    #키 안에 옷 값 추가 

    cnt = 1
    for i in dic.keys() :
        cnt *= len(dic[i]) + 1 # 가능한 경우의 수는 각 종류에 있는 옷 수 + 1을 모두 곱한 값
    print(cnt - 1)  #에서 1을 뺀 값이다.
