# 숫자 카드 게임
# 숫자가 쓰인 카드 N x M 형태로 놓여있다
# 뽑고자 하는 N행 먼저 선택 후 가장 숫자가 낮은 카드 뽑는다
# 이때 가장 높은 숫자를 뽑도록 하게 코딩하기

n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split())) # 한줄씩 입력받아 확인
    # min_value = min(data) # 현재 줄에서 가장 작은 수 찾기
    # result = max(result, min_value) # 가장 작은 수 중에서 큰 수 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)
    
print(result)

# 3 3
# 3 1 2
# 4 1 4
# 2 2 2
# result = 2
