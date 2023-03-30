str = input()
bomb = input()
bomb_length = len(bomb)
stack = []
for char in str:
    stack.append(char)
    
    if len(stack) < bomb_length:
        continue
    
    if ''.join(stack[-bomb_length:]) == bomb:
        while ''.join(stack[-bomb_length:]) == bomb:
            for _ in range(bomb_length):
                stack.pop()
       
if ''.join(stack) == "":
    print("FRULA")
else:
    print(''.join(stack))
    