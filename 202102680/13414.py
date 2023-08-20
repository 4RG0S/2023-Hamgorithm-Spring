import sys

k, l = map(int, input().split())

# 학번과 순서를 key, value 로 저장
dict = {}
for i in range(l):
    dict[input().rstrip()] = i

# 순서를 기준으로 오름차순 정렬
result = sorted(dict.items(), key=lambda x: x[1])

# 제한 인원보다 신청 인원이 적을 경우
if k > len(result):
    #k = len(result)
    for elem in result:
        print(elem[0])
else:
    # 학번을 제한 인원만큼 출력
    for i in range(k):
        print(result[i][0])