from sys import stdin

lst = list(stdin.readline().strip())
move = []
for _ in range(int(stdin.readline())):
    change = stdin.readline().split()
    if change[0] == 'L':
        if lst:
            move.append(lst.pop())
    elif change[0] == 'D':
        if move:
            lst.append(move.pop())
    elif change[0] == 'B':
        if lst:
            lst.pop()
    else:
        lst.append(change[-1])

print(''.join(lst+move[::-1]))
