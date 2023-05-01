testcase = int(input())

for _ in range(testcase):
    result = 0

    x1, y1, x2, y2 = (map(int, input().split()))
    n = int(input())
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        d1 = (cx-x1)**2 + (cy-y1)**2
        d2 = (cx-x2)**2 + (cy-y2)**2

        if r**2 < d1:   #d1 밖
            if r**2 > d2: #
                result += 1
            else :
                result += 0
        else:
            if r**2 < d2:
                result += 1
        
    print(result)