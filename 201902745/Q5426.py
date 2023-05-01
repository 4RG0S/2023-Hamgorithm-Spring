for _ in range(int(input())):
    S = input()
    len_S = len(S)
    li = [S[i:i+int(len_S**(1/2))] for i in range(0,len_S, int(len_S**(1/2)))]
    res = []
    for i in range(int(len_S ** (1 / 2) - 1), -1, -1):
        for j in range(int(len_S**(1/2))):
            res.append(li[j][i])
    result = ''
    for i in res:
        result += i
    print(result)
