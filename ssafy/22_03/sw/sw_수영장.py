def dfs(now, sum_price):
    global min_sum
    if now >= 12:
        if min_sum > sum_price:
            min_sum = sum_price
        return
    if now > min_sum:
        return
    dfs(now + 1, sum_price + price_lst[0] * plan_lst[now])
    dfs(now + 1, sum_price + price_lst[1])
    dfs(now + 3, sum_price + price_lst[2])
    dfs(now + 12, sum_price + price_lst[3])

for tc in range(1, int(input()) + 1):
    price_lst = list(map(int, input().split()))
    plan_lst = [0] + list(map(int, input().split()))
    # min_sum = 1000000
    # dfs(1, 0)
    # print(f'#{tc} {min_sum}')
    D = [0] * 13
    for i in range(1, 13):
        min_price = D[i - 1] + price_lst[0] * plan_lst[i]
        min_price = min(min_price, D[i - 1] + price_lst[1])
        if i >= 3:
            min_price = min(min_price, D[i - 3] + price_lst[2])
        if i >= 12:
            min_price = min(min_price, D[i - 12] + price_lst[3])
        D[i] = min_price
    print(f'#{tc} {D[12]}')