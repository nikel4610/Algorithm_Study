# N 입력받기
n = int(input())
# 전체 번호 입력받아서 집합 자료형에 기록
array = set(map(int, input().split()))

# M 입력받기
m = int(input())
# 전체 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 번호를 하나씩 확인
for i in x:
    # 해당 번호 존재 여부 확인
    if i in array:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
        
