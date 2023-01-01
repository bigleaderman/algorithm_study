from sys import stdin

alpha = ['A', 'B', 'C', 'D', 'E', 'F']
valid = [[0] * 6 for _ in range(6)]
conf = 1
first = stdin.readline().strip()
before = [alpha.index(first[0]), int(first[1]) - 1]
for i in range(35):
    now = stdin.readline().strip()
    cal = [abs(before[0] - alpha.index(now[0])), abs(before[1] - int(now[1]) + 1)]
    if not valid[alpha.index(now[0])][int(now[1]) - 1] and ((cal[0] == 2 and cal[1] == 1) or (cal[0] == 1 and cal[1] == 2)):
        valid[alpha.index(now[0])][int(now[1]) - 1] = 1
    else:
        conf = 0
        break
    before = [alpha.index(now[0]), int(now[1]) - 1]
cal = [abs(alpha.index(first[0]) - alpha.index(now[0])), abs(int(first[1]) - int(now[1]))]
if conf and ((cal[0] == 2 and cal[1] == 1) or (cal[0] == 1 and cal[1] == 2)):
    print('Valid')
else:
    print('Invalid')