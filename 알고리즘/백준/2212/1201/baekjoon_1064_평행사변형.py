from sys import stdin

x1, y1, x2, y2, x3, y3 = map(int, stdin.readline().split())

dif_x1 = x1 - x2
dif_x2 = x2 - x3
dif_x3 = x3 - x1
dif_y1 = y1 - y2
dif_y2 = y2 - y3
dif_y3 = y3 - y1
conf1, conf2 = 0, 0
if not dif_y1:
    conf1 = 1
if not dif_y2:
    conf2 = 1

if conf1 and conf2:
    print(-1)
elif conf1 or conf2:
    sum1 = dif_x1 ** 2 + dif_y1 ** 2
    sum2 = dif_x2 ** 2 + dif_y2 ** 2
    sum3 = dif_x3 ** 2 + dif_y3 ** 2
    now_list = [sum1 ** (1 / 2), sum2 ** (1 / 2), sum3 ** (1 / 2)]
    now_list.sort()
    print(abs(2 * (now_list[0] - now_list[2])))
elif dif_x1/dif_y1 == dif_x2/dif_y2:
    print(-1)
else:
    sum1 = dif_x1 ** 2 + dif_y1 ** 2
    sum2 = dif_x2 ** 2 + dif_y2 ** 2
    sum3 = dif_x3 ** 2 + dif_y3 ** 2
    now_list = [sum1 ** (1 / 2), sum2 ** (1 / 2), sum3 ** (1 / 2)]
    now_list.sort()
    print(abs(2 * (now_list[0] - now_list[2])))
