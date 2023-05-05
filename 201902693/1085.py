x, y, w, h = map(int, input().split())
input_list = [[x, y], [w, h]]
temp_list = [abs(x - w), abs(y - h), x, y]
print(min(temp_list))