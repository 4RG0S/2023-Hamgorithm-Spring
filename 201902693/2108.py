import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n) :
    lst.append(int(input()))

# lst정렬
lst.sort()

# result1 : 산술평균
# lst의 요소 합에서 개수 나눠주면 됨. 
# 소수점 첫째 자리에서 반올림
result1 = round(sum(lst) / len(lst))
print(result1)

# result2 : 중앙값
# 입력n은 홀수이기 때문에 2로 나눈 몫이 lst의 index로 들어가면
# 중앙값이 됨
result2 = lst[len(lst) // 2]
print(result2)

# result3 : 최빈값(최빈값이 여러개면 두 번째로 작은 수 출력)
# lst의 원소가 1개면 최빈값 1개로 결정되므로 그냥 출력
# 이외엔 Counter를 이용하여 세주고,
# most_common(2)로 많이 나온 수 2개를 뽑음
# 둘이 count한 횟수가 같으면 최빈값이 여러개 인 것으로 2번째 작은 수 출력
# 다르면 최빈값이 1개이므로 가장 많이 나온 수 출력
if len(lst) == 1 :
    print(lst[0])
else :
    cnt = Counter(lst)
    result3 = cnt.most_common(2)
    if result3[0][1] == result3[1][1] :
        print(result3[1][0])
    else :
        print(result3[0][0])

#result4 : 범위(최댓값 - 최솟값)
result4 = lst[-1] - lst[0]
print(result4)