# delta 탐색을 이용
delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]

for tc in range(1, int(input()) + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = [10000, 0]    #앞은 처음 idx값이고 뒤에는 최대cnt
    for a in range(N):  # 전체 순회하기
        for b in range(N):
            stack = [[a, b]]    #현재 위치를 idx를 stack에 넣기
            cnt = 1 # cnt 숫자를 1로 지정
            while stack:
                now = stack.pop()
                now_i = now[0]
                now_j = now[1]
                now_value = lst[now_i][now_j]
                for i, j in delta:
                    new_i = now_i + i
                    new_j = now_j + j
                    if 0 <= new_i < N and 0 <= new_j < N and lst[new_i][new_j] - lst[now_i][now_j] == 1:
                        cnt += 1
                        stack.append([new_i, new_j])
            if cnt >= max_cnt[1]:
                if cnt == max_cnt[1]:
                    if max_cnt[0] > lst[a][b]:
                        max_cnt[0] = lst[a][b]
                else:
                    max_cnt = [lst[a][b], cnt]
    print(f'#{tc}', max_cnt[0], max_cnt[1])


