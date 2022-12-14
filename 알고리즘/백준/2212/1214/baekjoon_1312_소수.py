A, B, N = map(int, input().split())
answer = 0
for i in range(N):
    A = A % B * 10
    answer = A // B
print(answer)