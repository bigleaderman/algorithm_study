import sys
sys.stdin = open('monster.txt', 'r')

# 전체 행렬의 순열 구하기
def f(k):
    if k == home_len * 2:
        stack.append([A[N[j]] for j in range(home_len * 2)])
    for i in range(k, home_len * 2):
        N[i], N[k] = N[k], N[i]
        f(k+1)
        N[i], N[k] = N[k], N[i]


for tc in range(1, int(input()) + 1): # test case
    num = int(input())  # arr 수
    arr = [list(map(int, input().split())) for _ in range(num)]
    home_len = 0 # 집과 몬스터의 가장 큰수 찾기
    for i in range(num):
        if home_len < max(arr[i]):
            home_len = max(arr[i])
    # 사람과 몬스터의 위치 찾기
    people = [0] * home_len
    monster = [0] * home_len
    min_cnt = 999999
    for i in range(num):
        for j in range(num):
            if arr[i][j]:
                if arr[i][j] > 0:
                    monster[arr[i][j] - 1] = [i, j]
                else:
                    people[abs(arr[i][j]) - 1] = [i, j]

    # stack에 리스트 순서대로 gate idx 순서 순열이 들어가있다.
    A = [i for i in range(1, home_len + 1)] + [-i for i in range(1, home_len + 1)]
    N = [i for i in range(home_len * 2)]
    stack = []
    f(0)
    road = []

    # stack에서 순서가 올바른것만 골라서 나오기
    for i in range(len(stack)):
        check = []
        for j in range(home_len * 2):
            if stack[i][j] < 0:
                if abs(stack[i][j]) not in check:
                    break
            check.append(stack[i][j])
        if len(check) == home_len * 2:
            road.append(check)

    # road의 순서대로 사냥하기
    for r in road:
        cnt = 0
        now = 0, 0
        for i in r:
            if cnt > min_cnt:
                break
            if i > 0:
                x, y = monster[i-1][0], monster[i-1][1]
                cnt += abs(now[0] - x) + abs(now[1] - y)
                now = x, y
            else:
                x, y = people[-i-1][0], people[-i-1][1]
                cnt += abs(now[0] - x) + abs(now[1] - y)
                now = x, y
        if min_cnt > cnt:
            min_cnt = cnt
    print(f'#{tc} {min_cnt}')



