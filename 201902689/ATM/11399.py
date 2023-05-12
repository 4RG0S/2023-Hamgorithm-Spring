import heapq
N = int(input())
times = list(map(int, input().split(' ')))
heapq.heapify(times)
result = []
tmp = 0

while times:
    # 이전 사람까지 돈을 인출하는 데 걸리는 시간 + 자신이 돈을 인출하는데 걸리는 시간 -> 내가 총 인출하는데까지 걸리는 시간
    tmp += heapq.heappop(times)
    # 사람마다 걸리는 시간을 배열에 더해줌
    result.append(tmp)
print(sum(result))
