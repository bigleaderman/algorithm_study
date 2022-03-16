def enq(item):
    global last
    last += 1
    tree[last] = item

    c = last
    p = c // 2

    while p and tree[p] < tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c // 2

def deq():
    global last
    tmp = tree[1]
    tree[1] = tree[last]
    last -= 1

    p = 1
    c = p * 2

    while c <= last:
        if c + 1 <= last and tree[c+1] > tree[c]:
            c += 1
        if tree[c] > tree[p]:
            tree[p], tree[c] = tree[c], tree[p]
            p = c
            c = p * 2
        else:
            break
    return tmp


# 최대힙
last = 0 # 힙의 원소 갯수
arr = [4, 15, 13, 11, 19, 20, 23]
tree = [0] * 10
enq(4)
enq(15)
enq(13)
enq(11)
enq(19)
enq(20)
enq(23)
print(tree)
while last != 1:
    print(deq(), tree)