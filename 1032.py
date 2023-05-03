n = int(input())
input_lst1 = list(input())
for i in range(n - 1) :
    input_lst2 = list(input())
    for j in range(len(input_lst1)) :
        if input_lst1[j] != input_lst2[j] :
            input_lst1[j] = '?'
print(''.join(input_lst1))