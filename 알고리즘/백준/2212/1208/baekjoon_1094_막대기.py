from sys import stdin

X = int(stdin.readline())

now = 64
count = 1
n = 64
while now != X:
    n = n // 2

    if now - n >= X:
        now -= n

    else:
        count += 1
print(count)

