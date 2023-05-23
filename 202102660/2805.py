n, want = map(int, input().split(" "))
trees = list(map(int, input().split(" ")))
# print(trees)
def check(num):
    hsum = 0
    for h in trees:
        hsum += (h-num if h>num else 0)
    return hsum >= want

start = 0
end = max(trees)

while start+1 < end:
    mid = (start+end)//2
    if check(mid):
        start = mid
    else :
        end = mid

print(start)