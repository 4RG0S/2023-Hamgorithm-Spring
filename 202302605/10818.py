n = int(input())
m = list(map(int, input().split()))

m.sort()
print(m[0], m[(n-1)])