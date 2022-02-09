# 순차 탐색 소스코드 구현
def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인하며
    for i in range(n):
        # 현재 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1 # 현재 원소의 위치를 반환

print(" 생성할 원소 개수를 입력하세요.")
input_data = input().split()
n = int(input_data[0]) # 원소의 개수
target = input_data[1] # 찾고자 하는 원소

print("앞서 적은 원소 개수만큼 문자열 입력.")
array = input().split()

#결과 출력
print("원소의 위치:", sequential_search(n, target, array))
