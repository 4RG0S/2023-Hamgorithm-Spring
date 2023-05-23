m = int(input())

for i in range(m):
    n = int(input())
    dict = {}
    for j in range(n):
        cloth = list(input().split())
        if cloth[1] in dict:
            dict[cloth[1]].append(cloth[0])
        else:
            dict[cloth[1]] = [cloth[0]]

    result = 1 # 각 종류마다 항목의 개수

    for k in dict:
        result *= (len(dict[k])+1)
    print(result-1)