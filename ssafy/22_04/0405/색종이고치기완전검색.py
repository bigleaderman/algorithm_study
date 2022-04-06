from sys import stdin

def check(i, j, n):
    if i + n <= 10 and j + n <= 10:
        total = 0
        # 붙일 색종의 크기 만큼 1이 있는지 확인
        for k in range(n):
            total += sum(arr[i + k][j:j + n])
        # 붙일 색종이가 알맞은 크기이면  cnt를 더하고 그 페이퍼를 뺀다
        if total == n ** 2:
            return True
    else:
        return False

def find(s):
    global min_cnt
    for i in range(s, 10):
        for j in range(10):
            if arr[i][j]:
                for paper in range(5, 0, -1):
                    if papers[paper-1] and check(i, j, paper):
                        papers[paper-1] -= 1
                        for a in range(paper):
                            for b in range(paper):
                                arr[i+a][j+b] = 0
                        find(i)
                        papers[paper - 1] += 1
                        for a in range(paper):
                            for b in range(paper):
                                arr[i+a][j+b] = 1


arr = [list(map(int, stdin.readline().split())) for _ in range(10)]
min_cnt = 9999
papers = [5, 5, 5, 5, 5]
print(-1 if min_cnt == 9999 else min_cnt)