import sys
input = sys.stdin.readline
a, b = map(int, input().split())
temp_lst = [x for x in range(1, a + 1)]
result = []
cnt = 1
while True :
    if len(temp_lst) == 0 :
        break
    if cnt % b == 0 :
        result.append(temp_lst.pop(0))
        cnt += 1
    else :
        temp = temp_lst.pop(0)
        temp_lst.append(temp)
        cnt += 1
        
print('<' , end="")    
for i in range(len(result)) :
    if i < len(result) - 1 :
        print(result[i] , ', ', sep = '', end="")
    else :
        print(result[i], end="")
print('>', end="")