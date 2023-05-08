import sys
n = int(input())
RGB = []

for i in range(n):
    RGB.append(list(map(int, input().split())))

result = sys.maxsize

def dp(rr,gg,bb):
    R, G, B = [0 for i in range(n)], [0 for i in range(n)], [0 for i in range(n)]
    R[0], G[0], B[0] = rr, gg, bb
    for i in range(1, n):
        r, g, b = RGB[i]
        R[i] = r + min(G[i-1], B[i-1])
        G[i] = g + min(R[i-1], B[i-1])
        B[i] = b + min(R[i-1], G[i-1])
    
    
    result = sys.maxsize
    
    if rr == sys.maxsize:
        result = min(result, R[-1])
    if gg == sys.maxsize:
        result = min(result, G[-1])
    if bb == sys.maxsize:
        result = min(result, B[-1])
    return result



print(min(dp(RGB[0][0], sys.maxsize, sys.maxsize), dp(sys.maxsize, RGB[0][1], sys.maxsize), dp(sys.maxsize, sys.maxsize, RGB[0][2])))