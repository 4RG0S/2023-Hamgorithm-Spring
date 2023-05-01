num = int(input())
# set은 search에 O(1)의 시간이 걸린다.
num_arr = set(map(int, input().split(' ')))

q = int(input())
q_arr = list(map(int, input().split(' ')))

for i in q_arr:
    if i in num_arr:
        print(1)
    else:
        print(0)
