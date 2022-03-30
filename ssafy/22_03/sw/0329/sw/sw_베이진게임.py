
def perm(n, k, player):
    global flag
    # 순열
    if k == 3:
        if babyjin[0] == babyjin[1] == babyjin[2]:
            flag = 1
            return
        if babyjin[0] + 1 == babyjin[1] and babyjin[1] + 1 == babyjin[2]:
            flag = 1
            return
    else:
        for j in range(len(player)):
            if not visited[j]:
                visited[j] = 1
                babyjin[k] = player[j]
                perm(n, k + 1, player)
                visited[j] = 0



for tc in range(1, int(input()) + 1):
    lst = list(map(int, input().split()))
    player1, player2 = [], []
    babyjin = [0] * 3
    visited = [0]*6
    flag = 0
    for i in range(len(lst)):
        if i % 2:
            player2.append(lst[i])
        else:
            player1.append(lst[i])
        if len(player1) >= 3:
            perm(len(player1), 0, player1)
            if flag:
                break
        if len(player2) >= 3:
            perm(len(player1), 0, player2)
            if flag:
                flag = 2
                break
    print(f'#{tc} {flag}')