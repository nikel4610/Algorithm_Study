# 선택 정렬 소스코드
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    # 가장 작은 원소의 인덱스
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    # 위치 바꾸기
    array[i], array[min_index] = array[min_index], array[i]
print(array)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 스와프(Swap) 소스코드
# array = [3, 5]
# array[0] , array[1] = array[1], array[0]
# [5, 3]
