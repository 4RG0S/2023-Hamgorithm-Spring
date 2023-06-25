N, M = map(int, input().split(' '))

arr = []

def backtracking():
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, N + 1):
        if arr:
            if arr[-1] <= i:
                arr.append(i)
                backtracking()
                arr.pop()
        else:
            arr.append(i)
            backtracking()
            arr.pop()

backtracking()

# print("############## backtraking2 ################")
# arr2 = []
# def backtracking2(start):
#     if len(arr2) == M:
#         print(' '.join(map(str, arr2)))
#         return
#     for i in range(start, N + 1):
#         arr2.append(i)
#         backtracking2(i)
#         arr2.pop()

# backtracking2(1)