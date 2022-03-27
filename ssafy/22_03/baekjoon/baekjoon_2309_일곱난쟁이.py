def f(now, num, lst, new_lst):
    # 젤 처음 나온 한개만 출력해주기 위해서 답이 나온경우 모두 return
    if new_lst:
        return
    # 갯수가 7이고 합이 100일때 출력
    if num == 7 and sum(lst) == 100:
        new_lst = lst
        new_lst.sort()
        for n in new_lst:
            print(n)
    # num이 7이나 끝까지 돌아도 7개를 못채울 경우 return
    if num == 7 or 10 - now + len(lst) < 7:
        return
    # 계속 반복적으로 돌면서 재귀호출
    for i in range(now, 10):
        lst.append(height[i])
        f(i+1, num + 1, lst, new_lst)
        lst.pop()

height = [0] + [int(input()) for _ in range(9)]
new_lst = []
nanjang = f(1, 0, [], new_lst)