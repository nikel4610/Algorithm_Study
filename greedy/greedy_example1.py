# 그리디 알고리즘
# 500원 100원 50원 10원 동전을 사용해서 거슬러줄 동전 최소 개수
# 거슬러 줘야 할 돈은 10의 배수

n = 1260 # 손님이 가진 돈
count = 0

coint_types = [500, 100, 50, 10]

for coin in coint_types:
    count += n // coin # coin_types 로 거슬러 줄 수 있는 동전 갯수
    n %= coin
    
print(count) # answer = 6
