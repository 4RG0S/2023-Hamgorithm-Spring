a = int(input())
b = int(input())
c = int(input())

temp_list = []
result = []
for i in range(len(str(a*b*c))):
    temp_list.append(str(a*b*c)[i])

for i in range(10):
    result.append(temp_list.count(str(i)))

for i in range(10):
    print(result[i])