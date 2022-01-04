# 8 x 8 크기의 체스판 위에 나이트는 2가지 방법으로 이동한다
# 1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동
# 2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동
# 나이트의 위치가 주어졌을 때 이동할 수 있는 경우의 수 출력하기
# 행 위치는 1 ~ 8, 열 위치는 a ~ h 로 표현

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동 가능한 8가지 방향
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# steps 이동 가능한지 확인
result = 0
for step in steps:
    # 이동 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 위치 이동 가능하면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
