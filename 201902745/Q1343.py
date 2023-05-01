board = input()
result = []
nTrue = True
for i in board.split('.'):
    if i == '':
        result.append('.')
    else:
        len_i = len(i)
        if len_i % 2 != 0:
            nTrue = False
            break
        else:
            while len_i > 0:
                if len_i >= 4:
                    result.append('A' * 4)
                    len_i -= 4
                elif len_i == 2:
                    result.append('B' * 2)
                    len_i -= 2
            result.append('.')
if nTrue:
    for i in range(len(result)):
        if len(result) -1 == i:
            break
        print(result[i], end='')
else:
    print(-1)


