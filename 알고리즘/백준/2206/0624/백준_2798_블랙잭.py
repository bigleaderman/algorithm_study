from sys import stdin

# 부분순열을 구하기 위해서 브루투포스를 이용해서 전체 탐색을 한다.
def dfs(n, i, total): # n은 카드선택 횟수, 고른 카드 다음 idx, total은 이때 동안 총합
    global max_num
    # 가지치기(total이 M을 넘으면 return)
    if total > M:
        return

    # 종료조건
    if n == 3:
        # total값을 비교해서 maximun 갱신
        if total > max_num:
            max_num = total

    # 부분수열을 구하기 위해서 반복 재귀
    else:
        for j in range(i, N):
            dfs(n+1, j+1, total + lst[j])


# 입력값 받기
N, M = map(int, stdin.readline().split())
lst = list(map(int, stdin.readline().split()))
max_num = 0

# 부분순열 탐색 시작
for i in range(N-2):
    dfs(1, i+1, lst[i])

print(max_num)