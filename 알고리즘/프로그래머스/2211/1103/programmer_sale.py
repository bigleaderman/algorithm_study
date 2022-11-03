def solution(want, number, discount):
    answer = 0
    count_list = [0] * len(want)
    want_dict = {}

    for i in range(len(want)):
        want_dict[want[i]] = i
    for i in range(10):
        if discount[i] in want:
            count_list[want_dict[discount[i]]] += 1

    if count_list == number:
        answer += 1
    for i in range(10, len(discount)):
        if discount[i - 10] in want:
            count_list[want_dict[discount[i - 10]]] -= 1
        if discount[i] in want:
            count_list[want_dict[discount[i]]] += 1
        if count_list == number:
            answer += 1

    return answer