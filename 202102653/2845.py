class TooManyInputError(Exception):
    def __init__(self):
        message = 'too many values entered\n'
        super().__init__(message)


class NotEnoughInputError(Exception):
    def __init__(self):
        message = 'not enough values entered\n'
        super().__init__(message)


NUMBER_OF_MEDIA = 5
try:
    number_of_people_in_unit, area = input().split()
    number_of_people_in_unit = int(number_of_people_in_unit)
    area = int(area)
except ValueError as e:
    print('Error occurred!\n', e)
    exit(1)

real_number_of_people = number_of_people_in_unit * area

try:
    media_list = list(map(int, input().split()))
    if len(media_list) < NUMBER_OF_MEDIA:
        raise NotEnoughInputError
    elif len(media_list) > NUMBER_OF_MEDIA:
        raise TooManyInputError
except Exception as e:
    print('Error occurred!\n', e)
    exit(1)

media_comparison_list = []

for i in range(0, 5):
    media_comparison_list.append(media_list[i] - real_number_of_people)

for i in range(0, 5):
    print(media_comparison_list[i], end=' ')
print()
