def solution(s):
    change = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    answer = ''
    word = ''
    for i in s:
        if i.isdigit():
            answer += i
            continue
        word += i
        if word in change:
            answer += change[word]
            word=''
    return int(answer)

def solution(s):
    num_list = ['ze', 'on', 'tw', 'th', 'fo', 'fi', 'si', 'se', 'ei', 'ni']
    answer = ''
    now = 0
    while now < len(s):
        if s[now].isdigit():
            answer += s[now]
            now += 1
        else:
            num = num_list.index(s[now : now + 2])
            if num in [1, 2, 6]:
                answer += str(num)
                now += 3
            elif num in [0, 4, 5, 9]:
                answer += str(num)
                now += 4
            else:
                answer += str(num)
                now += 5
    return answer

print(solution("one4seveneight"))