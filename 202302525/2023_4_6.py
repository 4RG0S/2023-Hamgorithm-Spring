while True:
    x = input()

    if(x == '0'):
        break
    
    else:
        a = list(x)
        count = 0 #자릿수
        z = 0  #key
        x = int(x)

        while True: #자릿수
          x = x//10
          count += 1

          if(x == 0):
              break
      
    if(count == 1):
        z = 1

    else:
        for k in range(0, count):
            if(int(a[k]) == int(a[count-k-1])):
                z = 1

            else:
                z = 0
                break

    if(z == 1):
        print("yes")

    else:
        print("no")