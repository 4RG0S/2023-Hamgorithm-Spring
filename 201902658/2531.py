import sys

num_sushi, _, sushi_to_eat, coupon_sushi = map(int, sys.stdin.readline().rsplit())
sushi_types = [int(sys.stdin.readline().rstrip()) for _ in range(num_sushi)]
start_ptr, end_ptr = 0, 0
max_variety = 0

while start_ptr != num_sushi:
    end_ptr = start_ptr + sushi_to_eat
    current_sushi_set = set()
    can_add_coupon = True

    for i in range(start_ptr, end_ptr):
        i %= num_sushi
        current_sushi_set.add(sushi_types[i])
        if sushi_types[i] == coupon_sushi: can_add_coupon = False

    current_variety = len(current_sushi_set)
    if can_add_coupon: current_variety += 1
    max_variety = max(max_variety, current_variety)
    start_ptr += 1

print(max_variety)
