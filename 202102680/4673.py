number = set(range(1, 10000))
remove = set()
for num in number:
    for n in str(num):
        num += int(n)
    remove.add(num)  # add: 집합에 요소를 추가할 때

result = number - remove  # set의 '-' 연산자로 차집합을 구함
for elem in sorted(result):  # sorted 함수로 정렬
    print(elem)