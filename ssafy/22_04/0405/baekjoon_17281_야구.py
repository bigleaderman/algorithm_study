from sys import stdin

def count_score(real_player):
    global max_cnt
    # 점수
    cnt = 0
    # 타선을 알려주는 순서
    sequence = 0
    for now_ining in ining:
        out = 0
        # 주자가 현재 어디있는지 판단
        b1, b2, b3 = 0, 0, 0
        while out != 3:
            # 타순을 돌아가면서 플레이
            # 아웃
            now_player = now_ining[real_player[sequence]]
            if not now_player:
                out += 1
            # 1루타
            elif now_player == 1:
                cnt += b3
                b1, b2, b3 = 1, b1, b2
            elif now_player == 2:
                cnt += (b2 + b3)
                b1, b2, b3 = 0, 1, b1
            elif now_player == 3:
                cnt += (b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 1
            else:
                cnt += (b1 + b2 + b3 + 1)
                b1, b2, b3 = 0, 0, 0
            sequence = (sequence + 1) % 9
    max_cnt = max(max_cnt, cnt)


def parm(k):
    if k == 8:
        real_player = player[:3] + [0] + player[3:]
        count_score(real_player)
    else:
        for i in range(1, 9):
            if not visited[i]:
                visited[i] = 1
                player.append(i)
                parm(k+1)
                player.pop()
                visited[i] = 0

N = int(stdin.readline())
visited = [0] * 9
player = []
max_cnt = 0
ining = [list(map(int, input().split())) for _ in range(N)]
parm(0)
print(max_cnt)