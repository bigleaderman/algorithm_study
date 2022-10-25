def solution(numbers, hand):
    number_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    left_i, left_j = 3, 0
    right_i, right_j = 3, 2
    answer = ''
    for num in numbers:
        for i in range(len(number_list)):
                if num in number_list[i]:
                    num_i = i
                    break
        if num in [2, 5, 8, 0]:
            num_j = number_list[i].index(num)
            left_sum = abs(left_i - num_i) + abs(left_j - num_j)
            right_sum = abs(right_i - num_i) + abs(right_j - num_j)
            if left_sum > right_sum:
                right_i, right_j = num_i, num_j
                answer += 'R'
            elif left_sum < right_sum:
                left_i, left_j = num_i, num_j
                answer += 'L'
            else:
                if hand == "right":
                    right_i, right_j = num_i, num_j
                    answer += 'R'
                else:
                    left_i, left_j = num_i, num_j
                    answer += 'L'
        elif num in [1, 4, 7, '*']:
            left_i, left_j = num_i, 0
            answer += 'L'
        else:
            right_i, right_j = num_i, 2
            answer +='R'
    return answer