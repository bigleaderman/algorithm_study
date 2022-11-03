def solution(k, ranges):
    answer = []
    num_list = [k]
    while k != 1:
        if k % 2:
            k = k * 3 + 1
        else:
            k /= 2
        num_list.append(k)
    plus_list = []

    for i in range(len(num_list) - 1):
        plus_list.append((num_list[i] + num_list[i + 1]) / 2)

    for now_list in ranges:
        s, minus = now_list[0], now_list[1]
        e = len(plus_list) + minus
        if s > e:
            answer.append(-1)
        else:
            answer.append(sum(plus_list[s:e]))
    return answer