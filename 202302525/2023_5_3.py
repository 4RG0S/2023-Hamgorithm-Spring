n = int(input())
table = [[0 for col in range(0)] for row in range(50)]

for i in range(n):
    word = input()
    table[len(word)-1].append(word)

for i in table:
    if i == []:
        continue
    
    i = list(set(i))
    i.sort()

    
    for j in i:
        print(j)