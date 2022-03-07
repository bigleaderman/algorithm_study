for tc in range(1, int(input())+1):
    bit = list(map(int,input()))
    new_bit = [0]*len(bit)
    cnt = 0
    for i in range(len(bit)):
        if bit[i] != new_bit[i]:
            cnt += 1
            for j in range(i,len(bit)):
                new_bit[j] = bit[i]
    print(f'#{tc} {cnt}')

