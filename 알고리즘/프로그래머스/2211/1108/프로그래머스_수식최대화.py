from itertools import permutations


def solution(expression):
    def calculate(a, b, operation):
        if operation == "*":
            return a * b
        elif operation == "+":
            return a + b
        elif operation == "-":
            return a - b

    answer = 0
    list_seq = permutations(['*', '-', '+'])
    for now in list_seq:
        first_list = expression.split(now[0])
        first_operation = [0] * len(first_list)

        for i in range(len(first_list)):
            second_list = first_list[i].split(now[1])
            second_operation = [0] * len(second_list)

            for j in range(len(second_list)):
                third_list = second_list[j].split(now[2])
                if len(third_list) == 1:
                    second_operation[j] = int(third_list[0])
                else:
                    for k in range(len(third_list) - 1):
                        if not k:
                            num = calculate(int(third_list[k]), int(third_list[k + 1]), now[2])
                        else:
                            num = calculate(num, int(third_list[k + 1]), now[2])
                    second_operation[j] = num
            if len(second_list) == 1:
                first_operation[i] = second_operation[0]
            else:
                for k in range(len(second_list) - 1):
                    if not k:
                        num = calculate(second_operation[k], second_operation[k + 1], now[1])
                    else:
                        num = calculate(num, second_operation[k + 1], now[1])
                first_operation[i] = num

        for k in range(len(first_list) - 1):
            if not k:
                num = calculate(first_operation[k], first_operation[k + 1], now[0])
            else:
                num = calculate(num, first_operation[k + 1], now[0])
        if abs(num) > answer:
            answer = abs(num)

    return answer