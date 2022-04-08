def find(n):
    for i in range(5):
        for j in range(5):
            if mine_row[i][j] == n:
                mine_row[i][j] = 0
                mine_col[j][i] = 0
                if i == j:
                    mine_cross[0][i] = 0
                if i+j == 4:
                    mine_cross[1][i] = 0

def check():
    cnt = 0
    for r in mine_row:
        if not sum(r):
            cnt+=1
    for c in mine_col:
        if not sum(c):
            cnt+=1
    for cross in mine_cross:
        if not sum(cross):
            cnt+=1
    return cnt

def answer():
    global cnt
    for num in call:
        for n in num:
            cnt += 1
            find(n)
            if cnt >= 12:
                if check() >= 3:
                    return cnt

mine_row = [list(map(int, input().split())) for _ in range(5)]
mine_col = [[1]*5 for _ in range(5)]
mine_cross = [[1]*5 for _ in range(2)]
cnt = 0
call = [list(map(int, input().split())) for _ in range(5)]
print(answer())
