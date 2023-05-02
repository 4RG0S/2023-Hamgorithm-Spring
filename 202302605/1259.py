while True:
    a = input()    

    num = [0] * len(a)
    re = [0] * len(a)
    
    
    if a == '0':
        break
    else:
        for i in range(len(a)):
            num.append(int(a[i]))
            re.insert(0, int(a[i]))

    if num == re:
        print('yes')
    else:
        print('no')