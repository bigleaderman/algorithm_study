import sys
sys.stdin = open('wordread.txt', 'r')

for tc in range(1, int(input()) + 1):
    word_list = [[''] for _ in range(5)]
    word = [list(input()) for _ in range(5)]
    new_word = ''
    for i in range(5):
        word_list[i] = word[i] + [''] * (15-len(word[i]))
    word_list = list(map(''.join, zip(*word_list)))
    for j in range(len(word_list)):
        new_word += word_list[j]
    print(f'#{tc} {new_word}')