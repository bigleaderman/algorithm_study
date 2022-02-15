import sys
sys.stdin = open('input (6).txt', 'r')

for tc in range(int(input())):
    ladder = [list(map(int, input().split())) for _ in range(100)]
    a = 0
    for i in range(100):
        if ladder[99][i] == 2:
            start = [99, i]
            while True:
                start[0] -= 1
                print(start)
                if start[0] == 0:
                    print(f'#{tc+1} {start[1]}')
                    a = 1
                    break
                if ladder[start[0]][start[1] + 1] == 1 and start[1] != 99:
                    while True:
                        start[1] += 1
                        if ladder[start[0]][start[1]+1] == 0:
                            break

                if ladder[start[0]][start[1] - 1] == 1 and start[1] != 0:
                    while True:
                        start[1] -= 1
                        if ladder[start[0]][start[1]-1] == 0:
                            break


