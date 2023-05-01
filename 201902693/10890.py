input_list = []
for i in range(10):
    input_list.append(int(input()))
for i in range(len(input_list)) :
    input_list[i] = input_list[i] % 42
result_list = list(set(input_list))
print(len(result_list))