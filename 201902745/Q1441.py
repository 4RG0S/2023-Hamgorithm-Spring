from itertools import combinations

def is_Similar(s1, s2):
    s = []
    for i in [s1, s2]:
        alpha = []
        a = ""
        for j in i:
            if j not in alpha:
                alpha.append(j)
            a += str(alpha.index(j))
        s.append(a)
    if len(set(s)) == 1:
        return True
    return False

ans = 0
for i in combinations([input() for i in range(int(input()))], 2):
    if is_Similar(i[0], i[1]):
        ans += 1
print(ans)
