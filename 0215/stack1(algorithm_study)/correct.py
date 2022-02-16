import sys
sys.stdin = open('sample_input (3).txt', 'r')

for tc in range(int(input())):
    word_list = []
    for i in input():
        if i == '(' or i == '{':
            word_list.append(i)
        if i == ')':
            if word_list[-1]=='(':
                word_list.pop()
            else:
                print(f'#{tc+1} {0}')
        if i == '}':
            if word_list[-1]=='{':
                word_list.pop()
            else:
                print(f'{tc+1} {0}')
        print(word_list)
    if word_list:
        print(f'#{tc+1} {0}')
    else:
        print(f'#{tc+1} {1}')