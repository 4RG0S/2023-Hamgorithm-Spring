import sys
input = sys.stdin.readline
s = int(input())
cnt = 0
temp = 0
while True :
    if temp == s :
        print(cnt)
        break
    elif temp > s :
        print(cnt - 1)
        break
    else :
        cnt += 1
        temp += cnt

# 리스트 이용해서 cnt를 계속 리스트에 넣고, sum으로 리스트로 조건문 돌리면 시간초과
# 구글 정답
# s = int(input())
# n = 1
# while n * (n + 1) / 2 <= s:
#     n += 1
# print(n - 1)
# 그냥 합의 공식 쓰면 쉬운데 어렵게 풂