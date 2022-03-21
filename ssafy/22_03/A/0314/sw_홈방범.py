import sys
sys.stdin = open('home.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    house_cnt = 0

    for i in range(N):
        house_cnt += lst[i].count(1)
    max_cost = house_cnt * M
    max_cnt = 1

    for K in range(2, N+2):
        cost = K * K + (K - 1) * (K - 1)

        # 가지치기 모든 집을 다한 다고 가정을 해도
        # max_cost가 cost보다 작을 때는 홈 방범 서비스를 진행 할 수 없으므로 break하고 이전값이 최대값
        if cost > max_cost:
            break

        # N이 홀수 일때와 N이 짝수일 때 모든 범위를 감쌀 수 있는 max_cnt가 다르다.
        # 그리고 어차피 모든 범위를 감쌀 수 있으면 max_cnt는 house_cnt가 된다는 가정을 넣었다.
        elif K == N:
            if N % 2:
                max_cnt = house_cnt
        elif K == N+1:
            if not N % 2:
                max_cnt = house_cnt


        for i in range(N):
            for j in range(N):
                cnt = 0
                #중간 부터 위
                for a in range(-K + 1, 1):
                    for b in range(-a+1-K, K+a):
                        x, y = i + a, j + b
                        if 0 <= x < N and 0 <= y < N and lst[x][y]:
                            cnt += 1
                # 중안 아래 부터 쭉
                for a in range(1, K):
                    for b in range(-K + a + 1, K -a):
                        x, y = i + a, j + b
                        if 0 <= x < N and 0 <= y < N and lst[x][y]:
                            cnt += 1
                if max_cnt < cnt and cnt * M >= cost:
                    max_cnt = cnt
    print(f'#{tc} {max_cnt}')

