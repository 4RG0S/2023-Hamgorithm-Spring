from sys import stdin
T = int(stdin.readline())
num = 1
for i in range(T):
    student = int(stdin.readline())
    id = [int(stdin.readline().rstrip()) for _ in range(student)]
    divisor = 1
    while 1:
        result = set()
        for j in id:
            result.add(j%divisor)
        if len(result) == student:
            break
        else:
            divisor += 1
    print(divisor)
   
