import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
lst = [x for x in range(1, n + 1)]
lst = deque(lst)

#답은 결국 list로는 시간초과를 해결할 수 없어서
#deque를 사용해야 하는 것이었다.
#deque는 양방향 queue로 
#필요한 연산들이 모두 O(1)이라서
#list에 비해 매우 빨랐다.
while len(lst) > 1 :
    lst.popleft()
    lst.append(lst.popleft())
    
print(lst[0])

#시간초과 1
#del list의 시간복잡도는 O(n)이라
#아래 코드는 복잡도가 O(n**2)임
# lst = [x for x in range(1, n + 1)]
# while True :
#     del lst[0]
#     if len(lst) == 1 :
#         break
#     lst.append(lst[0])
#     del lst[0]
# print(*lst)


#시간초과 2
#list.pop()은 시간복잡도가 O(1)인줄 알았는데
#list.pop(i)는 똑같이 O(n)이었다.
# lst = [x for x in range(1, n + 1)]
# while True :    
#     lst.pop(0)
#     if len(lst) == 1 :
#         break
#     lst.append(lst.pop(0))
# print(lst[0])

#시간초과 3
#pop을 index안쓰고 하기 위해 lst를 뒤집어서 만들고
#시도했는데 insert때문에 결국 시간초과
# lst = [x for x in range(n, 0, -1)]
# while True :
#     lst.pop()
#     if len(lst) == 1 :
#         break
#     lst.insert(0, lst.pop())
# print(lst[0])