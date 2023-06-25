s = input()

if 'c=' in s :
    s = s.replace('c=', '.')
if 'c-' in s :
    s = s.replace('c-', '.')
if 'dz=' in s :
    s = s.replace('dz=', '.')
if 'd-' in s :
    s = s.replace('d-', '.')
if 'lj' in s :
    s = s.replace('lj', '.')
if 'nj' in s :
    s = s.replace('nj', '.')
if 's=' in s :
    s = s.replace('s=', '.')
if 'z=' in s :
    s = s.replace('z=', '.')
    
print(len(s))

# 그냥 해당 문자열들 리스트에 넣고 for문 돌리면서 i in s로 비교하면 더 쉬운데 
# 너무 하나씩 다했다.