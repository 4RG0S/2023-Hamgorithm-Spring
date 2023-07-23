n, k = map(int, input().split())
arr = list(map(int, input().split()))
result, temp = [], []
e = 0

def count(arg:list) -> int:
    for i in arg:
        if i == -1:
            return False
        
    return True

test = [k for _ in range(10)]

for start in range(n):
    while count(test) and e < len(arr):
        t = arr[e]

        test[t-1] -= 1        
        temp.append(t)
        e += 1

    if not count(test):
        test[t-1] += 1
        e-=1
        del temp[-1]

    # print(temp)
    result.append(len(temp))

    test[temp[0]-1] += 1
    del temp[0]

result.sort(reverse=True)

print(result[0])