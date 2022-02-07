# 큰 수 부터 작은 수의 순서로 내림차순 정렬하는 프로그램 만들기
# 첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다
# 둘째 줄부터 N + 1 번째 줄 까지 N개의 수가 입력된다

n = int(input()) # N 입력받기

# N 개의 정수를 리스트에 저장
array = []
for i in range(n):
    array.append(int(input()))
array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')

# 3
# 15
# 27
# 12
# 27 15 12
