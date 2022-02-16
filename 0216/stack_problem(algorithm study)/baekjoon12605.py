from sys import stdin

for tc in range(int(input())):
    word_list = input().split()
    word_list.reverse()
    new_word = ' '.join(word_list)
    print(*word_list)