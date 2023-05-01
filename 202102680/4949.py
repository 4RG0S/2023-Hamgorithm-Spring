while True:
    inp = input()
    stack = []
    if inp == '.':
        break
    for i in inp:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append('no')
                break
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append('no')
                break
        elif i == '.':
            break
        else:
            continue
    if len(stack) == 0:
        print('yes')
    else:
        print('no')