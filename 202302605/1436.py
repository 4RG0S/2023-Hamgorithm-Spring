n = int(input())
count = 0
six = 666

while True:
    if '666' in str(six):
        count += 1
        # six를 str형으로 변환하여 만약 그 안에 666이 포함되어 있다면
        # count를 1 증가 시킨다.

    if count == n:
        print(six)
        break
        # 그렇게 증가시킨 count가 입력받은 n과 같아지면 변수 six를 출력
        # 그리고 while문을 탈출. 

    six += 1
    # count가 n과 같아 질 때까지 정수 six를 1씩 증가
    # ex) 667, 668, ... 1666까지 계속 증가 시킴.
    # 2번째 666까지 반복문을 1천번 ㅋㅋㅋ
    # 되게 무식한 방법. but, 효과는 확실.