# 두개의 배열 A와 B 에서 K번 바꿔치기 연산을 수행하는데 바꿔치기 연산이란 배열A에 있는 원소 하나와 배열 B에 있는 원소
# 하나를 골라 서로 바꾸는 것을 말한다
# 최종 목표는 배열A의 모든 원소의 합이 최대가 되도록 하는 것이다
# 최대 K번 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램 작성

n ,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() # 오름차순 정렬
b.sort(reverse = True) # 내림차순 정렬

# 첫번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교ㅕ
for i in range(k):
    if a[i] < b[i]: # a의 원소가 b의 원소보다 작은 경우
        a[i], b[i] = b[i], a[i] # 두 원소를 교체
    else:
        break # a의 원소가 b의 원소보다 크거나 같을 때, 반복문 탈출
print(sum(a))

# 5 3
# 1 2 5 4 3
# 5 5 6 6 5
# 26
