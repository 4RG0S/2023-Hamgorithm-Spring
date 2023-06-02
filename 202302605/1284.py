while True:
    leng = 2
    st = input()
    arr = list(st)
    
    if arr[0] == '0':
        break

    for i in range(len(arr)):
        if arr[i] == '1':
            leng += 2

        elif arr[i] == '0':
            leng += 4

        else:
            leng += 3       

    leng += len(arr)-1
    print(leng)