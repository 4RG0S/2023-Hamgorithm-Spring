temp_lst = []
for i in range(1, 1001) :
    temp_lst += ([i]*i)

a, b = map(int, input().split())
result = temp_lst[a-1:b]
print(sum(result))