a = int(input())
b = int(input())
c = int(input())

m = a * b * c

n = '%d' %m

for i in range(10):
    s = '%d' %i
    z = n.count(s)
    print(z)