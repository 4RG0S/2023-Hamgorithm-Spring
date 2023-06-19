num = int(input())

h = 0
for i in range(1, num+1):
    num = list(map(int, str(i)))
    if i < 100:
        h += 1  # 100보다 작으면 모두 한수
    elif num[0]-num[1] == num[1]-num[2]:
        h += 1  # x의 각 자리가 등차수열이면 한수
print(h)