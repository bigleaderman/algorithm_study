def solution(numbers):
    num_list = []

    for i in range(len(numbers)):
        num = 0
        now_num = numbers[i]
        total_num = 0
        while now_num != 0:
            num_list.append(now_num % 2)
            now_num = now_num // 2
            num += 1

        plus_zero = 0
        now = 0
        while num != 0:
            plus_zero += 2 ** now
            num = num // 2
            now += 1


        for i in range(plus_zero - len(num_list)):
            num_list.append(0)
    num_list.reverse()

    answer = []
    return answer

solution([58])