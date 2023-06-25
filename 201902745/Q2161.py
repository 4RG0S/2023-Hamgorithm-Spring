N = int(input())

N_list = [i+1 for i in range(N)]
result = []
while len(N_list) != 1:
    result.append(N_list.pop(0))
    N_list.append(N_list.pop(0))

for i in result:
    print(i, end = ' ')
print(N_list[0])
