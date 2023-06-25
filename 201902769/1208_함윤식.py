import bisect

def dfs(idx, sum):
    if idx  == len(num_list):
        return
    sum_list.append(sum + num_list[idx])
    dfs(idx+1, sum)
    dfs(idx+1, sum+num_list[idx])

N, S = map(int, input().split())

num_list = list(map(int, input().split()))
left_list, right_list = num_list[:len(num_list) // 2], num_list[len(num_list) // 2:]

sum_list = []
num_list = left_list
dfs(0, 0)
sum_list_copy = sum_list.copy()

sum_list = []
num_list = right_list
dfs(0, 0)

sum_list.sort()
sum_list_copy.sort()

count = 0
for i in sum_list_copy:
    if i == S:
        count += 1
        
for j in sum_list:
    if j == S:
        count += 1
        
for i in sum_list_copy:
    find = S - i
    count += bisect.bisect_right(sum_list, find) - bisect.bisect_left(sum_list, find)
            
print(count)