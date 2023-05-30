a, b ,v = map(int, input().split(" "))

rest = (v-a)%(a-b)

if rest == 0:
    day = (v-a)//(a-b)+1
else:
    day = (v-a)//(a-b)+2
print(day)

