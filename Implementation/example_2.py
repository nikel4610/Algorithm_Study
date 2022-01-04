# 00시 00분 00초 부터 N시 59분 59초 중 모든 시각 중에서 3이 하나라도
# 포함된 모든 경우의 수를 구하는 프로그램
# 0 <= N <= 23

n = int(input())

count = 0
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)

# 5
# 11475
