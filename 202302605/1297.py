import math

a, b, c = map(int, input().split())

h = int(math.sqrt(a**2*b**2/(b**2+c**2)))
w = int(math.sqrt(a**2*c**2/(b**2+c**2)))

print(h, w)