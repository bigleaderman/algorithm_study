n = int(input())
max_len = 0
for i in range(1, n+1):
    stack = [n, i]
    while True:
        number = stack[-2] - stack[-1]
        if number < 0:
            if len(stack) > max_len:
                max_len = len(stack)
                max_stack = stack
            break
        stack.append(number)
print(max_len)
print(*max_stack)
