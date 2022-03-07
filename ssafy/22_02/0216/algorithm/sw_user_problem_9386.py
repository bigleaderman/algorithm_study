for tc in range(int(input())):
    _ = input()
    max_total = 0
    total = 0
    for i in input():
        if int(i):
            total += 1
            if total > max_total:
                max_total = total
        else:
            total = 0
    print(f'#{tc+1} {max_total}')
