n = int(input())

sol = list(map(int, input().split()))
result = sol[0] + sol[-1]
result_1 = sol[0]
result_2 = sol[-1]
#결과는 우선 아무거나 세팅 해둠

for i in range(n-1):
    k = sol.pop(i) #기준용액 꺼내기

    s, e = 0, n-2 

    while s <= e:
        mid = (s + e) // 2
        cal = k + sol[mid] #기준용액 + 탐색용액

        if abs(cal) < abs(result): 
            result = cal

            result_1 = k
            result_2 = sol[mid]

        if abs(result) == 0:
            break
        
        if cal < 0:
            s = mid + 1

        else:
            e = mid - 1

    sol.insert(i, k) #기준용액을 다시 집어넣어준다


print(result_1, result_2)