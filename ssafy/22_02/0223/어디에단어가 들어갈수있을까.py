import sys
sys.stdin = open('어디에단어가들어갈수있을까.txt', 'r')

# for tc in range(1, int(input())+1):
#     n, k = map(int, input().split())
#     lst_row = [list(map(int, input().split())) for _ in range(n)]
#     lst_col = list(zip(*lst_row))
#     total = 0
#     for i in range(n):
#         for j in range(n-k+1):
#             if j == 0:
#                 if lst_row[i][j:k+j] == [1]*k and lst_row[i][k+j] == 0:
#                     total += 1
#                 if lst_col[i][j:k+j] == tuple([1]*k) and lst_col[i][k+j] == 0:
#                     total += 1
#             elif j == n-k:
#                 if lst_row[i][j-1] == 0 and lst_row[i][j:j+k] == [1]*k:
#                     total += 1
#                 if lst_col[i][j - 1] == 0 and lst_col[i][j:j+k] == tuple([1]*k):
#                     total += 1
#             else:
#                 if lst_row[i][j-1] == 0 and lst_row[i][j+k] == 0 and lst_row[i][j:j+k] == [1]*k:
#                     total += 1
#                 if lst_col[i][j - 1] == 0 and lst_col[i][j + k] == 0 and lst_col[i][j:j + k] == tuple([1]*k):
#                     total += 1
#     print(total)

for tc in range(1, int(input())+1):
    n, k = map(int, input().split())
    lst_row = [input().replace(' ','') for _ in range(n)]
    lst_col = list(map(''.join,list(zip(*lst_row))))
    cnt, word = 0, '1' * k
    for row in lst_row:
        for space in row.split('0'):
            if space == word:
                cnt += 1
    for col in lst_col:
        for space in col.split('0'):
            if space == word:
                cnt += 1
    print(f'#{tc} {cnt}')