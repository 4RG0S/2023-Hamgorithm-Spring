n = int(input())
#메모리 초과
# #1개 6개 12개 18개 24개 ...
# temp_list = [1]
# for i in range(1, n):
#     if n > 6 * i:
#         temp_list.append(6 * i)
# new_list = []
# for i in range(len(temp_list)):
#     if sum(temp_list[:i]) >= n:
#         new_list.append(i)
# print(new_list[0])
num = 1
count = 1
while n > num :
    num += 6 * count
    count += 1
print(count)