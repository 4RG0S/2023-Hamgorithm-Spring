import itertools

n, m = map(int, input().split())
input_list = list(input().split())

result = list(itertools.combinations(input_list,3))
result_list = []
for i in range(len(result)) :
    result_list.append(int(result[i][0]) + int(result[i][1]) + int(result[i][2]))

for i in range(len(result_list)):
    result_list[i] = result_list[i] - m

temp = [x for x in result_list if x <= 0]

print(m + max(temp))