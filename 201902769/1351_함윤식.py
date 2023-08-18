n, p, q = map(int, input().split())
m = {}

def calculate(n, p, q):
    if n == 0:
        return 1
    if m.get(n):
        return m[n]
    m[n] = calculate(n//p, p, q) + calculate(n//q, p, q)
    return m[n]

print(calculate(n, p, q))
# Hash를 이용해서 메모이제이션을 해준다.
# 재귀로 분할정복을 해준다.