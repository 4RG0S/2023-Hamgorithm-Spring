import heapq

n = int(input())
h = []
for _ in range(n):
    heapq.heappush(h, int(input()))     # 입력 받은 걸 다 h 에 넣어줌

ham_plus = 0

while len(h) > 1:
    temp = heapq.heappop(h)     # 제일 작은 처음 값 pop
    ham = heapq.heappop(h)      # 그 다음 작은 값 pop에서 ham 에 저장
    temp += ham                 # 작은 값끼리 더하고
    heapq.heappush(h, temp)     # 그 값을 다음 더할 때도 사용할 수 있게 h에 저장
    ham_plus += temp            # 그 값을 ham_plus에 저장

print(ham_plus)