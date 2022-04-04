from sys import stdin

# 모음이 무조건 들어가야한다
# 그리고 ord를 이용해서 이전 글자보다 ord수가 커야한다.

def parm(k): # k는 깊이, c는 config 값으로 모음이 들어가면 c가 1로 바꿀 예정이다.
    # p에 이미 0이 들어가있으므로 0 이후 값을 생각해서 1을 더해줌
    config1 = 0
    config2 = 0
    if k == L + 1:
        for alpha in p[1:]:
            if alpha in ['a', 'e', 'i', 'o', 'u']:
                config1 += 1
            else:
                config2 += 1
        if config1 and config2 >= 2:
            print(''.join(p[1:]))
        return
    else:
        for i in range(C):
            if not visited[i] and ord(alphabets[i]) > ord(p[k-1]):
                visited[i] = 1
                p.append(alphabets[i])
                parm(k+1)
                visited[i] = 0
                p.pop()

L, C = map(int, stdin.readline().split())
alphabets = list(stdin.readline().strip().split())
change = [ord(alpha) for alpha in alphabets]
change.sort()
alphabets = [chr(i) for i in change]
visited = [0] * C
p = ['0']
parm(1)