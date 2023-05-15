score = input()
arr = list(score)

def num(arr):
    if arr[0] == 'A':
        return 4.0
    
    elif arr[0] == 'B':
        return 3.0
    
    elif arr[0] == 'C':
        return 2.0
    
    elif arr[0] == 'D':
        return 1.0
     
    else:
        return 0.0

result = num(arr)

if len(arr) == 1:
    result = 0.0
elif arr[1] == '+':
    result += 0.3
elif arr[1] == '-':
    result -= 0.3

print(result)