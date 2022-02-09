# 첫째 줄에 정수 N이 주어진다
# 둘째 줄에는 공백으로 구분해서 N개의 정수가 주어진다
# 셋째 줄에는 정수 M이 주어진다
# 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다
# 첫째 줄에 공백으로 구분하여 각 정수가 존재하면 yes, 없으면 no를 출력한다

# 이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 적은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# N 입력
n = int(input())
# 전체 번호를 공백으로 구분하여 입력
array = list(map(int, input().split()))
array.sort() # 정렬 먼저 수행

# M 입력
m = int(input())
# 찾고자 하는 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 번호를 하나씩 확인
for i in x:
    # 존재하는지 확인
    result = binary_search(array, i, 0, n-1)
    # 존재하면 yes 출력
    if result != None:
        print('yes', end = '')
    # 존재하지 않으면 no 출력
    else:
        print('no', end = ' ')

# 5
# 8 3 7 9 2
# 3
# 5 7 9
# no yes yes
