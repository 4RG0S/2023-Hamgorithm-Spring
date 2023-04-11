a, b = map(int, input().split())

# 시간초과
# for i in range(min(a, b), 0 , -1) :
#     if a % i == 0 and b % i == 0:
#         print(i)

# for i in range(max(a, b), (a * b) + 1) :
#     if i % a == 0 and i % b == 0:
#         print(i)

def GCD(a, b):
    while (b):
        a, b = b, a % b
    return a

def LCM(a, b):
    result = (a * b) // GCD(a, b)
    return result

print(GCD(a, b))
print(LCM(a, b))