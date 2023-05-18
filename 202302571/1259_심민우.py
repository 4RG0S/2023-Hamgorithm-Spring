while True:
    inpt = input()
    if inpt == "0":
        break
    num1 = []
    num2 = []
    l = len(inpt)

    if l % 2 ==0:
        for i in range(l//2):
            num1.append(int(inpt[i]))
        for i in range(l-1, l//2-1, -1):
            num2.append(int(inpt[i]))
    else:
        for i in range(l//2):
            num1.append(int(inpt[i]))
        for i in range(l-1, l//2, -1):
            num2.append(int(inpt[i]))

    if num1==num2:
        print("yes")
    else:
        print("no")