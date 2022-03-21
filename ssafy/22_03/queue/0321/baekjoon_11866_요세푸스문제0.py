N, K = map(int, input().split())
# 나중에 join을 이용하기 위해서 미리 str을 받아오기
# 그리고 K만큼 움직일때 1이 없어지기 때문에 K-1을 0으로 미리 list에 넣기
lst = list(map(str, range(1, N + 1))) + [0] * (N * (K-1))
front, rear, asw = 0, N, 0
answer = [0] * N
# rear과 front가 같으면 아무것도 남아 있지 않은 상태가 되므로 중지
while rear != front:
    # K-1 만큼 뒤로 옮겨 주기
    for _ in range(K-1):
        lst[rear] = lst[front]
        rear, front = rear + 1, front + 1
    # 마지막 수는 answer에 append 하고 front만 1더하기
    answer[asw] = lst[front]
    front, asw = front + 1, asw + 1
# 출력 조건 맞추기 위해서 사용
result = ', '.join(answer)
print(f'<{result}>')


