n = int(input())
A,B,C,D = [],[],[],[]

# A,B,C,D 에 입력받아 각각 넣어줌
for _ in range(n):
    a,b,c,d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

# A, B 로 만들 수 있는 합을 모두 구하여 딕셔너리에 몇개 있는 지까지 저장
left_sum = dict()
for a in A:
    for b in B:
        left_sum[a+b] = left_sum.get(a+b, 0) + 1

count = 0

# C, D로 만들 수 있는 합을 모두 구하여 이에 -1 을 곱한 값이 (더하여 0을 만들 수 있는 값) 딕셔너리에 몇 개 있는 지를 확인하여 count에 더해줌
for c in C:
    for d in D:
        count += left_sum.get(-(c+d), 0)

print(count)