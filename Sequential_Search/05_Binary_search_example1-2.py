# N 입력받기
n = int(input())
array = [0] * 100001

# 전체 번호 입력 받아서 기록
for i in input().split():
    array[int(i)] = 1

# M 입력받기
m = int(input())
# 전체 번호 공백 구분하여 입력
x = list(map(int, input().split()))
# 번호 하나씩 확인하기
for i in x:
    # 해당 번호 존재하는지 확인
    if array[i] == 1:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')

# 5
# 8 3 7 9 2
# 3
# 5 7 9
# no yes yes
