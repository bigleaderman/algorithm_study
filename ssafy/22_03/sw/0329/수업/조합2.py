'''
for i1: 0 -> N-R+0
    for i1: 0 -> N-R+1
        for i1: 0 -> N-R+2
'''

a = [1, 2, 3, 4]
N = 4
R = 3
for i in range(0, N-R+1):
    for j in range(i+1, N-R+2):
        for k in range(j+1, N-R+3):
            print(a[i],a[j],a[k])