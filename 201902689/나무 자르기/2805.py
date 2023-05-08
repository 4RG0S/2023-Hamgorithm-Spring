tree_num, tree_len = map(int, input().split(' '))
trees = list(map(int, input().split(' ')))
low_len = 1
high_len = max(trees)

while low_len <= high_len:
    sum_of_tree = 0
    mid_len = (low_len + high_len) // 2

    for tree in trees:
        if tree < mid_len:
            continue
        sum_of_tree += tree - mid_len
    # 자른 나무의 합이 작으면 더 짧아야 함
    if sum_of_tree < tree_len:
        high_len = mid_len - 1
    # 자른 나무의 합이 필요한 길이보다 크면 절단기의 높이를 더 크게 설정한다.
    elif sum_of_tree > tree_len:
        result = mid_len
        low_len = mid_len + 1
    else:
        print(mid_len) 
        exit()
print(high_len)


# comment
# 이분 탐색시에 lower bound와 upper bound를 생각하자.
# 값이 커지면 tmp = tree - mid_len 해주는 것 조차 시간을 많이 잡아먹는다.
