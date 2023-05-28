n = int(input())
result = []
for _ in range(n) :
    ps = list(str(input()))
    for i in range(len(ps)) :
        if '(' in ps and ')' in ps :
            if ps.index('(') < ps.index(')') :
                del ps[ps.index('(')]
                del ps[ps.index(')')]
    if ps == [] :
        result.append('YES')
    else :
        result.append('NO')
print(*result, sep = '\n')
    
#스택 사용
# n = int(input())
# for _ in range(n) :
#     ps = list(str(input()))
#     st = []
#     flag = 0
#     for i in range(len(ps)) :
#         if ps[i] == '(' :
#             st.append(ps[i])
#         else :
#             if '(' in st :
#                 st.pop()
#             else :
#                 flag = 1
#     if st == [] :
#         if flag == 1:
#             print('NO')
#         else :
#             print('YES')
#     else :
#         print('NO')