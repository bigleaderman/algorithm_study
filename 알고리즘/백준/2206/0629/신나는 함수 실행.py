from sys import stdin

N = int(stdin.readline())
lst = list(map(int, stdin.readline().split()))
lst.sort()
s, e = 0, N-1

min_num = int(4e9)
answer = []
while e > s:
    total = lst[s] + lst[e]
    if abs(total) < min_num:
        min_num = abs(total)
        answer = [lst[s], lst[e]]

    if total >= 0:
        e -= 1

    elif total < 0:
        s += 1
print(*answer)