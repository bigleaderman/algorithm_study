# 암호코드를 idx 순서 순으로 secret에 lst로 저장
secret = [[0, 0, 0, 1, 1, 0, 1], [0, 0, 1, 1, 0, 0, 1], [0, 0, 1, 0, 0, 1, 1], [0, 1, 1, 1, 1, 0, 1],
          [0, 1, 0, 0, 0, 1, 1], [0, 1, 1, 0, 0, 0, 1], [0, 1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 0, 1, 1], [0, 1, 1, 0, 1, 1, 1], [0, 0, 0, 1, 0, 1, 1]]


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    lst = []
    # 행을 돌면서 1이 있는 곳을 우선 찾기
    for i in range(N):
        # 1일 있는 행이 아니면 pass
        if 1 not in arr[i]:
            continue
        # 만약 lst가 안에 들어가 있으면 break
        if lst:
            break
        # 젤 뒤가 1인 곳을 찾아서 56개의 숫자를 lst에 넣고 break
        for j in range(M-1, 0, -1):
            if arr[i][j] == 1:
                lst = arr[i][j - 55: j + 1]
                break
    # secret_num을 담을 list
    secret_num = []
    # 7개 씩 돌면서 암호와 일치하는 수를 secret_num에 push
    for i in range(0, len(lst), 7):
        now_lst = lst[i:i+7]
        for j in range(len(secret)):
            if now_lst == secret[j]:
                secret_num.append(j)
    # total을 0으로 하고
    total = 0
    # 암호에서 짝수인 부분이 상품고유 번호에서 홀수인 부분만 고르는 것이다.
    # 그래서 total에 더하기
    for i in range(len(secret_num)):
        if i % 2:
            total += secret_num[i]
        else:
            total += secret_num[i] * 3
    # total이 10으로 나누어 떨어지는지 안떨어지는지 확인
    if total % 10:
        print(f'#{tc} 0')
    else:
        print(f'#{tc}', sum(secret_num))