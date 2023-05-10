x = int(input())

n = 1

while x > n:
    x -= n
    n += 1

if n%2 == 0:
    a = x
    b = n-x+1
else:
    a = n-x+1
    b = x

print(f"{a}/{b}")