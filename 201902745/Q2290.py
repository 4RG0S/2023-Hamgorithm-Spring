S, N = map(int, input().split())

N = str(N)
M = 2 * S + 3

ans = [[" "] * ((S + 2) * (len(N)) + (len(N) - 1)) for _ in range(M)]

st = 0
for i in N:
    if i == '1':
        st += S + 1
        for j in range(1, 1 + S):
            ans[j][st] = "|"
        for j in range(2 + S, M - 1):
            ans[j][st] = "|"
        st += 2
    elif i == '2':
        for j in range(2 + S, M - 1):
            ans[j][st] = "|"
        st += 1
        for _ in range(S):
            ans[0][st], ans[(M - 1) // 2][st], ans[M - 1][st] = "-", "-", "-"
            st += 1

        for j in range(1, 1 + S):
            ans[j][st] = "|"
        st += 2
    elif i == '3':
        st += 1
        for _ in range(S):
            ans[0][st], ans[(M - 1) // 2][st], ans[M - 1][st] = "-", "-", "-"
            st += 1

        for j in range(1, 1 + S):
            ans[j][st] = "|"
        for j in range(2 + S, M - 1):
            ans[j][st] = "|"
        st += 2
    elif i == '4':
        for j in range(1, 1 + S):
            ans[j][st] = "|"
        st += 1
        for _ in range(S):
            ans[(M - 1) // 2][st] = "-"
            st += 1
        for j in range(1, 1 + S):
            ans[j][st] = "|"
        for j in range(2 + S, M - 1):
            ans[j][st] = "|"
        st += 2
    elif i == '5':
        for j in range(1, 1 + S):
            ans[j][st] = "|"
        st += 1
        for _ in range(S):
            ans[0][st], ans[(M - 1) // 2][st], ans[M - 1][st] = "-", "-", "-"
            st += 1
        for j in range(2 + S, M - 1):
            ans[j][st] = "|"
        st += 2
    elif i == '6':
        for j in range(1, 1 + S):
            ans[j][st] = "|"
        for j in range(2 + S, M - 1):
            ans[j][st] = "|"
        st += 1
        for _ in range(S):
            ans[0][st], ans[(M - 1) // 2][st], ans[M - 1][st] = "-", "-", "-"
            st += 1
        for j in range(2 + S, M - 1):
            ans[j][st] = "|"
        st += 2
    elif i == '7':
        st += 1
        for _ in range(S):
            ans[0][st] = "-"
            st += 1
        for j in range(1, 1 + S):
            ans[j][st] = "|"
        for j in range(2 + S, M - 1):
            ans[j][st] = "|"
        st += 2
    elif i == '8':
        for j in range(1, 1 + S):
            ans[j][st] = "|"
        for j in range(2 + S, M - 1):
            ans[j][st] = "|"
        st += 1
        for _ in range(S):
            ans[0][st], ans[(M - 1) // 2][st], ans[M - 1][st] = "-", "-", "-"
            st += 1
        for j in range(1, 1 + S):
            ans[j][st] = "|"
        for j in range(2 + S, M - 1):
            ans[j][st] = "|"
        st += 2
    elif i == '9':
        for j in range(1, 1 + S):
            ans[j][st] = "|"
        st += 1
        for _ in range(S):
            ans[0][st], ans[(M - 1) // 2][st], ans[M - 1][st] = "-", "-", "-"
            st += 1
        for j in range(1, 1 + S):
            ans[j][st] = "|"
        for j in range(2 + S, M - 1):
            ans[j][st] = "|"
        st += 2
    else:
        for j in range(1, 1 + S):
            ans[j][st] = "|"
        for j in range(2 + S, M - 1):
            ans[j][st] = "|"
        st += 1
        for _ in range(S):
            ans[0][st], ans[M - 1][st] = "-", "-"
            st += 1
        for j in range(1, 1 + S):
            ans[j][st] = "|"
        for j in range(2 + S, M - 1):
            ans[j][st] = "|"
        st += 2
for a in ans:
    print("".join(a))
