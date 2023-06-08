num_of_testcase = int(input())

result_list = []

for i in range(num_of_testcase):
    count = 0
    x_start, y_start, x_destination, y_destination = map(int, input().split())
    num_of_p_sys = int(input())
    for j in range(num_of_p_sys):
        x_p_sys, y_p_sys, radius_p_sys = map(int, input().split())
        dist_start = pow(pow(x_start - x_p_sys, 2) + pow(y_start - y_p_sys, 2), 0.5)
        dist_destination = pow(pow(x_destination - x_p_sys, 2) + pow(y_destination - y_p_sys, 2), 0.5)

        if (dist_start < radius_p_sys < dist_destination) \
                or (dist_start > radius_p_sys > dist_destination):
            count += 1
    result_list.append(count)

for result in result_list:
    print(result)
