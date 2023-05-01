while True:
  y=0
  i=0
  x=int(input())
  if(x==0):
   break
  else:
    a = [0]*5
    y=0
    count=0
    z = 0
    while True:
      y = x%10
      x = x//10 
      a[i]=y
      count=count+1
      if(x==0):
       break
      i=i+1
      
      
      
    if(count==1):
     print("yes")
     continue
    else:
      for k in range(0, count):
        if(a[k]==a[count-k-1]):
         z=1
        else:
         z=0
         break

    if(z==1):
     print("yes")
    else:
     print("no")