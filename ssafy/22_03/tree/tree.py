'''
4
1 2 1 3 3 4 3 5
'''
def pre(v):
    if v: # 0번 정점이 없으므로 0번은 자식이 없는 경우를 표시
        print(v)
        pre(ch1[v])
        pre(ch2[v])

def middle(v):
    if v:
        middle(ch1[v])
        print(v)
        middle(ch2[v])

def back(v):
    if v:
        back(ch1[v])
        back(ch2[v])
        print(v)

E = int(input())    # edge 수
arr = list(map(int, input().split()))
V = E + 1   # 정점 수 == 1번 부터 V번까지 정점이 있을때 마지막 정점

# 부모번호를 인덱스로 자식번호 저장
ch1 = [0] * (V + 1)
ch2 = [0] * (V + 1)
# 자식 번호를 인덱스로 부모번호를 저장
par = [0] * (V + 1)
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if not ch1[p]:
        ch1[p] = c
    else:
        ch2[p] = c
    par[c] = p
#
# pre(1)
# pre(2)
# middle(1)
# back(1)
'''
4
2 1 2 4 4 3 4 5
'''
# print(*par)
# root 찾기
root = 0
for i in range(1, V+1):
    if par[i]==0:
        root = i
        break
# print(root)

# 정점의 조상 찾기
c = 5
anc = []
while par[c] != 0:
    anc.append(par[c])
    c = par[c]
print(*anc)
