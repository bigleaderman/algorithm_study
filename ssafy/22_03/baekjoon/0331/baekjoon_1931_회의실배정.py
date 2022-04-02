from sys import stdin

N = int(stdin.readline())
lst = [list(map(int, stdin.readline().split())) for _ in range(N)]
cnt = 1
# 종료시간에 대해서 먼저 정렬하고, 시작 시간에 대해서 정렬한다. 이러면 시작하자 마자 끝나는 회의도 포함 가능
lst.sort(key=lambda x: (x[1], x[0]))
next = 1
now = 0
while next != len(lst):
    if lst[now][1] <= lst[next][0]:
        cnt += 1
        now = next
    next += 1
print(cnt)

