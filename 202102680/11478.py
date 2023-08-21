string =input()
answer = set() # set 이용해서 중복 제거

for i in range(len(string)):
    for j in range(i, len(string)):
        answer.add(string[i:j+1])   # i번째 문자 부터 부분 문자열

print(len(answer))  # set에 들어있는 갯수 출력