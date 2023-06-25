for _ in range(100):
    S = input().rstrip()
    if S == "*":
        break

    for index in range(1, len(S) - 1):
        check_not_sur = set()
        for i in range(len(S) - index):
            pair = S[i] + S[i + index]
            if pair in check_not_sur:
                print(S, "is NOT surprising.")
                break
            else:
                check_not_sur.add(pair)
        else:
            continue
        break
    else:
        print(S, "is surprising.")
