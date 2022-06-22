def solution(n, info):
    answer = []
    num = 0
    for i in range(len(n)):
        if info[i]:
            num += (10 - i)
    max_num = num + 1

    # dfs
    def dfs(last_num, now_info): # 남은 횟수, 현재정보, 현재까지 합
        nonlocal max_num, answer

        if
        if not last_num:
            if now_sum > max_num:
                max_num = now_sum
            elif now_sum == max_num:
                if answer:
                    now_info.sort()
                    for j in range(min(len(now_info), len(answer))):
                        if now_info[j][0] > answer[j][0]:

                else:


    for i in range(len(n)):
        lst = [0] * 11
        if info[i]:
            if info[i] == n:
                return [-1]
            else:
                lst[i] = info[i] + 1
                dfs(n - 1 - info[i], lst)
        else:
            lst[i] = 1
            dfs(n - 1, lst)

    return answer