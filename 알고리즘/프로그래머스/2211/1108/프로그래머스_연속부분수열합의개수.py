def solution(elements):
    sum_set = set()
    new_list = elements + elements
    for i in range(1, len(elements)+1):
        for j in range(len(elements)):
            sum_set.add(sum(new_list[j:j+i]))
    return len(sum_set)