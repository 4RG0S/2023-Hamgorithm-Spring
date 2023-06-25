def main():
    number_of_testcase = int(input())

    for i in range(number_of_testcase):
        # Input variables
        x_of_p1, y_of_p1, dist_p1_enemy, \
            x_of_p2, y_of_p2, dist_p2_enemy = \
            map(int, input().split())

        # Concentric and has the same radius length
        if x_of_p1 == x_of_p2 and y_of_p1 == y_of_p2 and dist_p1_enemy == dist_p2_enemy:
            print(-1)
            continue

        pow_dist_players = \
            pow(x_of_p1 - x_of_p2, 2) + pow(y_of_p1 - y_of_p2, 2)

        sum_dist_enemy = dist_p1_enemy + dist_p2_enemy

        pow_sub_dist_enemy = pow(dist_p1_enemy - dist_p2_enemy, 2)

        # Inscribed or circumscribed
        if pow_dist_players == pow(sum_dist_enemy, 2) or pow_dist_players == pow_sub_dist_enemy:
            print(1)
        # Has two intersection point
        elif pow(sum_dist_enemy, 2) > pow_dist_players > pow_sub_dist_enemy:
            print(2)
        else:
            print(0)


if __name__ == "__main__":
    main()


