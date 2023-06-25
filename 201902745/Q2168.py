def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


x, y = map(int, input().split())
x, y = max(x, y), min(x, y)

result = x + y - gcd(x, y)
print(result)
