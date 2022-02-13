# 절단기에 높이(H)를 지정하면 줄지어진 떡을 한번에 절단한다.
# 총 길이가 M일때 적어도 M만큼의 떡을 얻기위해 절단기에 설정할 수 있는 높이의
# 최댓값을 구하는 프로그램을 작성하시오.

# 떡의 개수(N)와 요청한 떡의 길이(M)를 입력받는다.
n, m = list(map(int, input().split(' ')))
# 각 떡의 개별 높이 정보 입력받기.
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로 result에 기록
        start = mid + 1
print(result)

# 4 6
# 19 15 10 17
# 15
