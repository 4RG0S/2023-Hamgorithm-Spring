l_result = [0] * 10
u_result = [0] * 10
l, u = map(int, input().split())
l -= 1
digit = 1
result = 0

while True:
    while l % 10 != 9: #떨이 뺌
        l_list = list(map(int, str(l)))
        for i in range(len(l_list)):
            l_result[l_list[i]] += digit
        l -= 1

    if l >= 10:
        for i in range(10):
            l_result[i] += (l // 10 +1) * digit

    else:
        for i in range(1, l+1):
            l_result[i] += digit
        break

    digit *= 10
    l //= 10

digit = 1
while True:
    while u % 10 != 9: #떨이 뺌
        u_list = list(map(int, str(u)))
        for i in range(len(u_list)):
            u_result[u_list[i]] += digit
        u -= 1

    if u >= 10:
        for i in range(10):
            u_result[i] += (u // 10 +1) * digit

    else:
        for i in range(1, u+1):
            u_result[i] += digit
        break
        

    digit *= 10
    u //= 10

for i in range(10):
    result += (u_result[i] * i) - (l_result[i] * i)

print(result)