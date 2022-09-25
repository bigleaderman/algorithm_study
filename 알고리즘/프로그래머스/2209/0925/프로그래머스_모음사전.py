from itertools import per
def solution(word):
    word_list = ['A', 'E', 'I', 'O', 'U']
    num = len(word)
    answer = 0
    for i in range(num):
        if i == 0:
            answer += word_list.index(word[i]) * 781 + 1
        elif i == 1:
            answer += word_list.index(word[i]) * 156 + 1
        elif i == 2:
            answer += word_list.index(word[i]) * 31 + 1
        elif i == 3:
            answer += word_list.index(word[i]) * 6 + 1
        elif i == 4:
            answer += word_list.index(word[i]) * 1 + 1
    return answer