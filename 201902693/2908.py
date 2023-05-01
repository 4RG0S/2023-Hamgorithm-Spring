a, b = map(str, input().split())
a_list = list(a)
b_list = list(b)
a_list.reverse()
b_list.reverse()

x, y = "", ""
for i in range(len(a_list)):
    x = x + a_list[i]
for i in range(len(b_list)):
    y = y + b_list[i]

if int(x) > int(y) :
    print(int(x))
else :
    print(int(y))