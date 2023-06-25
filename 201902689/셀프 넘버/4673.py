total = 10000

# 셀프 넘버
self_num = [True] * (total + 1)

for i, x in enumerate(self_num):
    if i == 0:
        continue
    if x:
        print(i)
        num = i
        while num <= total:
            num += sum(map(int, str(num)))
            if num <= total:
                self_num[num] = False
