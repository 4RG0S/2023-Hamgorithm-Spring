a, b, v = map(int,(input().split()))

#시간초과
# temp = 0
# count = 0
# while temp <= v:
#     temp += a
#     count += 1
#     if temp == v :
#         break
#     temp -= b
# print(count)

if (v - a) % (a - b) == 0:
    print((v - a) // (a - b) + 1)
    
else :
    print((v - a) // (a - b) + 2)