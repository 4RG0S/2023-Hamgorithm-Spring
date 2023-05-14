n = int(input())

for i in range(1,n+1):
    i_list = list(map(int,str(i)))
    num = sum(i_list)
    n_sum = num+ i
    if n_sum == n:
        print(i)
        break

    if i == n:
        print(0)