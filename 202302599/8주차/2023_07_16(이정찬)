N = int(input())

proty_value = list(map(int, input().split()))

proty_value.sort()

start = 0 
end = len(proty_value)-1

result = 10000000000 # 용액의 특성값의 최대값으로 설정해놓아 첫 실행시 밑 코드의 값으로 초기값을 정함.
answer = []

while not(start == end or start+1 == end or start == end-1) :
    temp_result = proty_value[start] + proty_value[end]

    if abs(temp_result) < abs(result) :
        result = temp_result
        answer = [proty_value[start],proty_value[end]]
    
    if temp_result == 0 :
        break
    elif temp_result > 0 : # 결과값은 0으로 향해야 하니 양수면 양수를 줄임.
        end -= 1
    elif temp_result < 0 : # 위와 동일 음수를 키움.
        start += 1

temp_result = proty_value[start] + proty_value[end] # while 조건식으로 인해 마지막 리스트 인덱스들이 확인되지 않았을 수 있기에 한번더 확인

if abs(temp_result) < abs(result) :
    result = temp_result

    answer = [proty_value[start],proty_value[end]] 


print(*answer) # 리스트 내 모든 원소 출력