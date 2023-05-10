import sys
input = sys.stdin.readline
n = int(input())
result = []
for i in range(1, n) :
    s = str(i)
    temp_lst = []
    for j in  s :
        temp_lst.append(int(j))
    if sum(temp_lst) + i == n:
        result.append(i)

if len(result) == 0 :
    print(0)
else : 
    print(result[0])


# 구글 정답
# i를 문자열로 바꾸고 j로 쪼개서 다시 정수 만들고 더하는거
# 보다 그냥 map이용하면 한번에 합을 구할 수 있다.
# 리스트 이용할 필요없이 break를 이용하면 된다.
# for문이 끝까지 돌면 생성자가 없는 것이므로 0을 출력
# n = int(input())

# for i in range(1, n+1): 
#     num = sum((map(int, str(i))))
#     num_sum = i + num  
    
#     if num_sum == n:
#         print(i)
#         break
#     if i == n: 
#         print(0)