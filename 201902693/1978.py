import math

n = int(input())

input_list = list(map(int, input().split()))
max_value = max(input_list)

dp = [0] * (max_value+1)


for i in range(2, int(math.sqrt(max_value)) + 1):
    for j in range(i+1, len(dp)):
        if j % i == 0:
            dp[j] = 1
dp[0], dp[1] = 1, 1

count = 0
for i in input_list :
    if dp[i] == 0:
        count += 1
print(count)

# for i in input_list:
#     if i == 1 :
#         input_list.remove(1)
#     for j in range(2, int(math.sqrt(i)) + 1) :
#         if i % j == 0:
#             input_list.remove(i)
# print(len(input_list))

