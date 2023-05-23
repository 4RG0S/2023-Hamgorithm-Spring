
have, goal = map(int, input().split(" "))

h_list = [
    int(input())
    for _ in range(have)
]

def check(mid):
    count = 0
    for line in h_list:
        count += line // mid
    if count >= goal:
        return True
    else:
        return False

start = 1
end = max(h_list)+1

while start+1 < end :
    mid = (start+end)//2

    if check(mid):
        start = mid
    else:
        end = mid

print(start)