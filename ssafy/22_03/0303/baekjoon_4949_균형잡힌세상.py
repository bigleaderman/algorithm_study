from sys import stdin

def f():
    stack = []
    for i in sentence:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if stack:
                if stack[-1] != '(':
                    return 'no'
                else:
                    stack.pop()
            else:
                return 'no'
        elif i == ']':
            if stack:
                if stack[-1] != '[':
                    return 'no'
                else:
                    stack.pop()
            else:
                return 'no'
    if stack:
        return 'no'
    else:
        return 'yes'

while True:
    sentence = list(stdin.readline())
    if sentence[0] == '.':
        break
    print(f())

