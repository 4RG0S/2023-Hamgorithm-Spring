while True : 
    A , B = map(int,input().split())
    if A < B :
        if B % A == 0 :
            print("factor")
        else :
            print("neither")
    if A > B :
        if A % B == 0 :
            print("multiple")
        else :
            print("neither")
    elif A == 0 and B == 0 :
        break