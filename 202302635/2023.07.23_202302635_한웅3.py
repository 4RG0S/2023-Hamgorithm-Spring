N = int(input())
a = list(map(int, input().split()))

a2 = sorted(list(set(a))) #set함수 이용 중복 제거
dic = {a2[i] : i for i in range(len(a2))} #딕셔너리를 이용
for i in a:
    print(dic[i], end = ' ')