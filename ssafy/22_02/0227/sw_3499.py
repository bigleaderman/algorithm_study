for tc in range(1, int(input())+1):
    n = int(input())
    word_lst = list(input().split())
    new_word_lst = []
    for i in range(n//2):
        if n % 2:
            new_word_lst.append(word_lst[i])
            new_word_lst.append(word_lst[n // 2 + 1 + i])
        else:
            new_word_lst.append(word_lst[i])
            new_word_lst.append(word_lst[n // 2 + i])
    if n % 2:
        new_word_lst.append(word_lst[n//2])
    print(f'#{tc}', *new_word_lst)