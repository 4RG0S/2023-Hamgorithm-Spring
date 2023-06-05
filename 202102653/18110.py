import sys


def round_off(target):
    if target - int(target) >= 0.5:
        return int(target)+ 1
    else:
        return int(target)


number_of_opinions = int(sys.stdin.readline())

difficulty = 0

if number_of_opinions != 0:
    opinion_list = []

    for i in range(0, number_of_opinions):
        opinion_list.append(int(sys.stdin.readline()))

    opinion_list.sort()

    # 제외할 사람의 수
    extreme_value = round_off(number_of_opinions * 3 / 20)

    for i in range(extreme_value, number_of_opinions - extreme_value):
        difficulty = difficulty + opinion_list[i]
    difficulty = round_off(difficulty / (number_of_opinions - 2 * extreme_value))

print(difficulty)

