testcase = int(input())

case = [[0 for i in range(2)] for j in range(testcase)] 

for i in range(testcase):
    case[i][0], case[i][1] = input().split()
    case[i][0] = int(case[i][0])
    case[i][1] = int(case[i][1])

def factorial(n):
    if n == 1 or n == 0:
        return 1
    
    if table[n] != 0:
        return table[n]
      
    else:
        table[n] = n * factorial(n-1)
        return table[n]

for i in range(testcase):
    n = case[i][0]
    table = [0]*(n+1)
    result1 = factorial(n)

    m = case[i][1]
    table = [0]*(m+1)
    result2 = factorial(m)

    result3 = factorial(m-n)

    print(int(result2/(result3 * result1)))