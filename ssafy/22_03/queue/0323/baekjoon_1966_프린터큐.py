from sys import stdin
from collections import deque

for _ in range(int(stdin.readline())):
    N, M = map(int, stdin.readline().split())
    # 현재 값이 idx를 파악하기 위해서 enumerate를 썼다.
    Q = deque(enumerate(list(map(int, stdin.readline().split()))))
    cnt = 0
    # M이 빠져나갈 때 까지 반복하기
    while True:
        cnt += 1
        max_value = 0
        # max_value와 비교해서 가장 큰 값을 찾기
        for i in range(len(Q)):
            if Q[i][1] > max_value:
                max_value = Q[i][1]
                pop_num = i

        # pop_num이 0이 아닐 때 -i만큼 돌려서 pop하기
        if pop_num:
            Q.rotate(-pop_num)
            now_pop = Q.popleft()
        else:
            now_pop = Q.popleft()

        # pop된 lst가 target과 같으면 break하기
        if now_pop[0] == M:
            break
    print(cnt)