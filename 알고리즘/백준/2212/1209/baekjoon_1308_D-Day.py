from sys import stdin

def select_config(now_year):
    if not now_year % 400:
        config = 1
    elif not now_year % 100:
        config = 0
    elif not now_year % 4:
        config = 1
    else:
        config = 0
    return config

start = list(map(int, stdin.readline().split()))
end = list(map(int, stdin.readline().split()))

standard = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
not_standard = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
answer = 0

if (end[0] - start[0] == 1000 and (start[1] < end[1] or (start[1] == end[1] and start[2] <= end[2]))) or end[0] - start[0]  > 1000:
    print('gg')
else:
    if start[0] == end[0]:
        now_year = start[0]
        config = select_config(now_year)
        if config:
            start_sum = sum(not_standard[:start[1]-1]) + start[2]
            end_sum = sum(not_standard[:end[1]-1]) + end[2]
            answer = end_sum - start_sum
            print(f'D-{answer}')
        else:
            start_sum = sum(standard[:start[1] - 1]) + start[2]
            end_sum = sum(standard[:end[1] - 1]) + end[2]
            answer = end_sum - start_sum
            print(f'D-{answer}')
    else:
        start_config = select_config(start[0])
        end_config = select_config(end[0])
        # 시작년도
        if start_config:
            start_sum = sum(not_standard[start[1]-1:]) - start[2]
            answer += start_sum
        else:
            start_sum = sum(standard[start[1] - 1:]) - start[2]
            answer += start_sum
        # 끝년도
        if end_config:
            end_sum = sum(not_standard[:end[1] - 1]) + end[2]
            answer += end_sum
        else:
            end_sum = sum(standard[:end[1] - 1]) + end[2]
            answer += end_sum
        for i in range(start[0] + 1, end[0]):
            if select_config(i):
                answer += 366
            else:
                answer += 365
        print(f'D-{answer}')