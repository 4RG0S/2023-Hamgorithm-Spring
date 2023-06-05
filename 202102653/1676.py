input_number = int(input())
cnt_divisor_two = 0
cnt_divisor_five = 0

for i in range(1, input_number + 1):
    while True:
        if i % 2 == 0:
            cnt_divisor_two += 1
            i /= 2
        else:
            break

    while True:
        if i % 5 == 0:
            cnt_divisor_five += 1
            i /= 5
        else:
            break

print(min(cnt_divisor_two, cnt_divisor_five))
