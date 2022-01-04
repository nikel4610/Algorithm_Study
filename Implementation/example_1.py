# 상하좌우
# N x N 크기의 정사각형 공간, 상 하 좌 우 로 이동하며 시작 좌표는 (1,1)
# L R U D 이동하여 최종 이동한 좌표 표시

n = int(input()) # N 입력받기
x, y = 1, 1
plans = input().split()

# L R U D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간 벗어나면 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny
print(x, y)
# 5
# R R R U D D
# 3 4
