import sys

K, N = map(int,input().split())

lan_cable = []

for _ in range(K) :
    lan_cable.append(int(sys.stdin.readline()))

    if lan_cable[len(lan_cable)-1] > lan_cable[0] : # 탐색을 빠르게 하기 위해 가장 큰 값을 인덱스 0번으로 이동시킴
        temp_cable = lan_cable[len(lan_cable)-1]
        lan_cable[len(lan_cable)-1] = lan_cable[0]
        lan_cable[0] = temp_cable

if lan_cable[0] == 1 : # 1인 경우에는 2로 나눌시 zerodivision이 발생함으로 따로 경우 설정
    mid_value = int(lan_cable[0])

    cal_value = int(lan_cable[0]) # 더하고 빼면서 기준 값에 연산 시킬 값
else :
    mid_value = int(lan_cable[0]/2)

    cal_value = int(lan_cable[0]/2)

temp_value_1 = 0 # 목표 랜선 개수에 달성하였으나, 최대값을 더 늘릴 수 있는 경우를 위해 만든 수
temp_value_2 = 0 

count = 0

while(True) :
    count = 0
    
    for i in lan_cable :
        count += int(i/mid_value)

    if count < N :

        if cal_value == 1 : # 위와 동일, zerodivison 방지용
            trash = 0
        else :
            cal_value = int(cal_value/2) 

        mid_value -= cal_value

    elif count > N :

        if mid_value == temp_value_1 : # 이전에 저장해둔 기준값과 현재값이 동일시, 루프를 돌고 있는것이니 탈출
            break

        temp_value_1 = mid_value
        mid_value += cal_value # 연산 후 값을 저장하면, 즉 바로 위에 있는 코드와 위치가 바뀌면 무한루프에 걸리니 유의
        
        
    elif count == N : 

        if mid_value == temp_value_2 :
            break

        temp_value_2 = mid_value

        if cal_value == 1 :
            trash = 0
        else :
            cal_value = int(cal_value/2)

        mid_value += cal_value

print(mid_value)