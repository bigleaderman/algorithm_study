from sys import stdin

galho = input().replace('()','.')
stack = []
total = 0
for i in galho:
    if i == '(':
        stack.append(i)
        total += 1
    elif i == ')':
        stack.pop()
    else:
        total += len(stack)
print(total)
