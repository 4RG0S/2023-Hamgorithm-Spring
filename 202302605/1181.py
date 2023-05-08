# n = int(input())
# arr = []
# arr.append(input())

# for i in range(n-1):
#     str = input()
    
#     if str in arr:
#         continue

#     if len(str) <= len(arr[0]):
#         arr.insert(0, str)

#     for j in range(len(arr), 0, -1):
#         if len(str) > len(arr[(j-1)]):
#             arr.insert(j, str)
#             break

# for k in range(len(arr)-1):
#     if len(arr[k]) < len(arr[k+1]):
#         print(arr[k])
         
#     elif len(arr[k]) == len(arr[k+1]):
#         ar = sorted([arr[k], arr[k+1]])
#         arr[k] = ar[0]
#         arr[k+1] = ar[1]
#         print(arr[k])
 
# print(arr[len(arr)-1])

# 위에는 내가 짠 개 쓰레기 코드 밑은 승주형



import sys

n = int(input())
arr = []
    
for i in range(n):
    arr.append(sys.stdin.readline().strip())

arr = set(arr)
arr = list(arr)
arr.sort()
arr.sort(key=len)

for i in range(len(arr)):
    print(arr[i])