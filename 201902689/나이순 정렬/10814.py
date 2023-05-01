num = int(input())
peoples = []
for i in range(num):
    age, name = input().split(' ')
    # 순서를 넣어놓는 생각 나쁘지 않았음
    peoples.append((int(age), i, name))
    # list의 0번과 1번 인덱스로 sort
peoples.sort(key=lambda x: (x[0], x[1]))
for people in peoples:
    print(people[0], people[-1])
