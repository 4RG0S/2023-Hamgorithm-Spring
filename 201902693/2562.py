input_list = []
for _ in range(9) :
    input_list.append(int(input()))
sorted_input_list = sorted(input_list)
print(sorted_input_list[-1])
print(input_list.index(sorted_input_list[-1]) + 1)