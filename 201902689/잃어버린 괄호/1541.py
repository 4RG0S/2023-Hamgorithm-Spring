input_str = input()

stack = list(input_str)
result = 0
plus = 0
minus = 0
oper = ["+", "-"]
tmp_str = ""

while stack:
    tmp = stack.pop()
    if not tmp in oper:
        tmp_str = tmp + tmp_str
    else:
        if tmp == "+":
            plus += int(tmp_str)
            tmp_str = ""
        else:
            plus += int(tmp_str)
            minus += plus
            plus = 0
            tmp_str = ""
if tmp_str != "": plus += int(tmp_str)
print(plus - minus)
