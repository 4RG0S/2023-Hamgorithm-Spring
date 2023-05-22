import sys
input = sys.stdin.readline
n = int(input())
lst = []

# n이 최대 10000까지 입력될 수 있는데 for문에서 얼마나 돌려야할지 
# 모르겠어서 10**10을 넣었는데 맞았다. 운이 좋았다.

for i in range(10**10) :
    if '666' in str(i) :
        lst.append(i)
    if len(lst) == n :
        break
        
print(lst[-1])

# 구글에서 찾아본 답안
# 역시나 for문을 돌리는게 좋은 방법은 아닌 것 같다.
# n에 따라 반복횟수가 결정되게 while문을 사용했다.
# result를 증가시키면서 666이 들어있으면 count를 해주고
# count가 n과 같으면 내가 찾는 값이므로 해당 result를 
# 출력해준다. 실행결과 내가 짠 코드보다 빨랐다. 836ms vs 680ms
# n = int(input())
# cnt = 0
# result = 666
 
# while True:
#     if '666' in str(result):
#         cnt += 1
 
#     if cnt == n:
#         break
 
#     result += 1
 
# print(result)