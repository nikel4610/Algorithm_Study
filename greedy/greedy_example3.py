# 큰 수의 법칙
# 첫째 줄에 N(2 <= N <= 1000), M(1 <= M <= 10000), K(1 <= K <= 10000)의 자연수가 주어지며
# 각 자연수는 공백으로 구분
# 둘째 줄에 N개의 자연수가 주어진다 (1 이상 10000이하)
# 입력으로 주어지는 K는 항상 M보다 작거나 같다
# 입력 예시 5 8 3         출력 예시 46
#          2 4 5 4 6

n, m, k = map(int, input().split()) # N, M, K 공백으로 구분하여 입력받기
data = list(map(int, input().split())) # N개의 수를 공백으로 구분하여 입력받기

data.sort() # 입력받은 수들 정렬
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두번째로 큰 수

result = 0

# while True:
#     for i in range(k): # 가장 큰 수를 K번 더하기
#         if m == 0: # M이 0 이면 break
#             break
#         result += first
#         m -= 1 # 더할때 마다 -1
#     if m == 0: # M이 0 이면 break
#         break
#     result += second # 두번째로 큰 수 더하기
#     m -= 1 # 더할때 마다 -1

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / ( k + 1 )) * k
count += m % ( k + 1 )

result += ( count ) * first # 가장 큰 수 더하기
result += ( m - count) * second # 두번째로 큰 수 더하기

print(result)

# 3 3
# 3 1 2
# 4 1 4
# 2 2 2
# result = 2
