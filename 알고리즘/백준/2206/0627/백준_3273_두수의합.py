from sys import stdin

N = int(stdin.readline())
lst = list(map(int, stdin.readline().split()))
lst.sort()
target = int(stdin.readline())

count = 0
s, e = 0, N-1
while e > s:
    total = lst[s] + lst[e]
    if total == target:
        count += 1
        s += 1

    elif total < target:
        s += 1

    else:
        e -= 1

print(count)



