# a,b,c,d,e,f,g,h = map(int, input().split())

# if a==1 and b==2 and c==3 and d==4 and e==5 and f==6 and g==7 and h==8:
#     print('ascending')
# elif a==8 and b==7 and c==6 and d==5 and e==4 and f==3 and g==2 and h==1:
#     print('descending')
# else:
#     print('mixed')

# 위에는 대가리 박은 코드

a = list(map(int, input().split()))
# = [int(i) for i in input().split()] 과 동일한 결과를 도출  

if a == sorted(a):
    # sorted는 sort와 달리 리스트 본체를 변환
    print('ascending')
elif a == sorted(a, reverse = True):
    print('descending')
else:
    print('mixed')

# 근데 a.sort()로는 왜 안되는지 모르겠음;;