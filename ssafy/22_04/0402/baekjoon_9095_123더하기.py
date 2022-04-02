from sys import stdin

def f(lst):
    global cnt
    if sum(lst) > num:
        return
    elif sum(lst) == num:
        cnt += 1
        return
    for i in range(1, 4):
        lst.append(i)
        f(lst)
        lst.pop()


N = int(stdin.readline())
for i in range(N):
    num = int(stdin.readline())
    cnt = 0
    f([])
    print(cnt)