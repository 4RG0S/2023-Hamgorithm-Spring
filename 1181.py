import sys
a = int(sys.stdin.readline())
input_list = []
# input_list = list(set(list(input() for _ in range(a))))
for i in range(a):
    input_list.append(sys.stdin.readline().strip())
input_list = list(set(input_list))
input_list.sort()

#버블정렬, 삽입정렬 이용해서 정렬하니 시간초과
# for end in range (1, len(input_list)):
#     for i in range(end, 0, -1):
#         if len(input_list[i-1]) > len(input_list[i]):
#             input_list[i-1], input_list[i] = input_list[i], input_list[i-1]     
#         elif len(input_list[i-1]) == len(input_list[i]) :
#             input_list[i-1:i+1] = sorted(input_list[i-1:i+1])

input_list.sort(key=len)

for i in range(len(input_list)):
    print(input_list[i])