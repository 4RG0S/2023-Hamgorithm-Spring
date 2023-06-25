x , y , w , h =map(int,input().split())
ls = []
ls.append(w-x)
ls.append(h-y)
ls.append(x-0)
ls.append(y-0)
print(min(ls))
