import sys
from collections import defaultdict

input_func = sys.stdin.readline
num_elements, max_occurrences = map(int, input_func().split())
elements = list(map(int, input_func().split()))

max_length = 0
left_ptr, right_ptr, count_dict = 0, 0, defaultdict(int)

while right_ptr < num_elements:
    # 해당 요소의 등장 횟수가 k 이하인 경우, 카운트 딕셔너리를 업데이트하고 right_ptr를 이동
    if count_dict[elements[right_ptr]] < max_occurrences:
        count_dict[elements[right_ptr]] += 1
        right_ptr += 1
    else:
        # 해당 요소의 등장 횟수가 k를 초과하는 경우, left_ptr의 요소를 카운트에서 제외하고 left_ptr를 이동
        count_dict[elements[left_ptr]] -= 1
        left_ptr += 1
    # 가장 긴 길이를 계산하여 max_length에 저장
    max_length = max(max_length, right_ptr - left_ptr)

print(max_length)
