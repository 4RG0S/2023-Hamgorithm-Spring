def dfs(idx, sum):
    global count
    if idx == len(num_list):
        return
    if sum + num_list[idx] == S:
        count += 1
    dfs(idx+1, sum)
    dfs(idx+1, sum+num_list[idx])

N, S = map(int, input().split())

num_list = list(map(int, input().split()))
count = 0
dfs(0, 0)
print(count)