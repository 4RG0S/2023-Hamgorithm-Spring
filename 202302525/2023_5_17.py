import sys 
n, m, b = map(int, input().split())
table = []
high = int(2e9)
tresult = 0
fresult = 0

for i in range(n):
    table.append(list(map(int, input().split())))

for i in range(257):
    add_block = 0
    sub_block = 0

    for j in range(n):
        for k in range(m):
            if table[j][k] < i:
                temp = i - table[j][k]
                sub_block += temp
                
            else:
                temp = table[j][k] - i
                add_block += temp

    if sub_block - add_block > b:
        continue
    
    time = add_block * 2 + sub_block
    
    if time <= high:
        high = time
        fresult = i

print(high, fresult)