from sys import stdin
from collections import deque

N = int(stdin.readline())
lst = deque()
for _ in range(N):
    word = stdin.readline().strip()
    if word[-1].isnumeric():
        word, num = word.split()
        if word == 'push_back':
            deque.append(lst, int(num))
        else:
            deque.appendleft(lst, int(num))
    else:
        if word == 'size':
            print(len(lst))

        elif word == 'empty':
            if len(lst):
                print(0)
            else:
                print(1)

        elif not len(lst):
            print(-1)

        else:
            if word == 'pop_front':
                print(deque.popleft(lst))

            elif word == 'pop_back':
                print(deque.pop(lst))

            elif word == 'front':
                print(lst[0])

            else:
                print(lst[-1])