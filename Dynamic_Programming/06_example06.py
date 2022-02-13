# N가지 종류의 화폐가 있다. 이 화폐를 최소한의 개수로 이용해서 그 가치의 합이
# M원이 되도록 한다. 이때 각 화폐는 몇 개라도 사용할 수 있으며ㅡ 사용한 화폐의 구성은
# 같지만 순서만 다른것은 같은 경우로 구분한다.

# 정수 N, M을 입력받기
n, m = map(int, input().split())
# N개의 화폐 단위 정보 입력받기
array = []
for i in range(n):
    array.append(int(input()))

# 한번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍 진행(바텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        # (i - k)원을 만드는 방법이 존재하는 경우
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)
# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])

# 2 15             3 4
# 2                3
# 3                5
# 5                7
#                  -1
