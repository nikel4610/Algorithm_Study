# 캐릭터는 1 x 1 크기로 동서남북 중 한 곳을 바라본다
# 월드는 N x M 크기의 직사각형이고 각각의 칸은 육지 또는 바다이다
# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향을 90도)부터 차례로 갈 곳을 정한다
# 2. 바로 왼쪽 칸에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 한칸 전진
#    왼족 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 하고 1단계로 돌아간다
# 3. 네 방향 모두 가본 칸이거나 바다로 된 칸인 경우 바라보는 방향을 유지한 채 한 칸 뒤로 가고 1단계로 돌아간다
#    단 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우 움직임을멈춘다
# 메뉴얼에 따라 움직인 후 캐릭터가 방문한 수를 출력
# 방향 -> 0:북쪽 1:동쪽 2:남쪽 3:서쪽 / 월드 -> 0:육지 1:바다

# N M 을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 방몬한 위치 저장하기 위해 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 x y 좌표 방향 입력받기
x, y , direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표

# 전체 맵 정보
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

#북 동 남 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
           x = nx
           y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)

# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1
# 3 (result)
