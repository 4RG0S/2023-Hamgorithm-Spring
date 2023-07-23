n = int(input())
num = list(map(int, input().split()))
numset = {i for i in num}
numset = list(numset)
numset.sort()  #입력으로 들어온 배열을 set으로 바꾸고 -> 다시 list -> sort 

def binary(arg): #이분탐색 수행 함수
    s, e = 0, len(numset) - 1

    while s <= e:
        mid = (s + e) // 2

        if numset[mid] == arg:
            break
        
        elif numset[mid] < arg:
            s = mid + 1

        else:
            e = mid - 1

    
    return mid #매개변수의 numset에서 index를 반환(압축된 결과) 

for i in num:
    print(binary(i), end = ' ')

