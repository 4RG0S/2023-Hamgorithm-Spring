n = int(input())
for i in range(n) :
    a, b = map(int, input().split())
    lst = list(map(int,input().split()))
    # cnt로 몇 번째로 빠져나가는지 체크
    cnt = 0
    # location으로 원하는 원소의 위치 찾기
    location = b
    
    while True :
        max_val = max(lst)
        # pop하기 전에 최대값 저장
        temp = lst.pop(0)
        # 가장 앞에 있는 원소 pop
        location -= 1
        # 가장 앞에 있는거 pop했으므로 위치 앞당겨짐
        
        if max_val == temp : # pop한 게 최대값이었으면
            cnt += 1 # 빠져나갔으므로 cnt 올림
            if location < 0 : # location이 음수가 되면 빠져나간게 원하는 값이기 때문에
                print(cnt) # cnt출력하고
                break # 반복문 탈출
            
        else : # pop한 게 최대값이 아니면
            lst.append(temp) # lst 맨 뒤에 붙임
            if location < 0 : # locaion이 음수가 되면 pop하고 맨 뒤에 붙인 거이기 때문에
                location = len(lst) - 1 # location을 lst의 맨 뒤 값으로
            
