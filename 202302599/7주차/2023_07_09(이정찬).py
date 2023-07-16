import sys
import heapq

negative = [] # 음수만 저장할 리스트
positive = [] # 양수만 저장할 리스트

N = int(input())

for _ in range(N) :

    i = int(sys.stdin.readline())

    if i > 0 : # 입력 받는 수가 양수인지 판단
        heapq.heappush(positive,i)

    elif i < 0 : # 입력 받는 수가 음수인지 판단
        heapq.heappush(negative,[-i,i]) # 다시 한번 음수로 표현한 값을 리스트로 묶어 저장. heap 내 리스트에서의 최소값 판단은 첫번째 원소로 함.

    else : # 위 둘다 해당이 안되면 입력받은 수가 0임.

        if len(positive) == 0 and len(negative) == 0 : # 두 리스트가 모두 비어있는지 확인
            print("0")

        elif len(negative) == 0 : # 음수 리스트만 비어있는지 확인
            print(heapq.heappop(positive))

        elif len(positive) == 0 : # 양수 리스트만 비어있는지 확인
            print(heapq.heappop(negative)[1])

        else : # 두 리스트 모두 차있는 경우

            if positive[0] < negative[0][0] :
                print(heapq.heappop(positive))
            
            else :
                print(heapq.heappop(negative)[1])
