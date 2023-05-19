while (True):
    str = input()
    if str == "0":
        break
    s1 = str[:len(str)//2]

    if len(str) % 2 == 0:
        # 길이가 짝수인 경우.
        s2 = str[len(str)//2:][::-1]
    else :
        s2 = str[len(str)//2+1:][::-1]
        # print(s2)
    if s1 == s2:
        print("yes")
    else :
        print("no")