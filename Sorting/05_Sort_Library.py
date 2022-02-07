array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
result = sorted(array)
# array.sort()
print(result)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

array1 = [('바나나', 2), ('사과', 5), ('당근', 3)]
def setting(data):
    return data[1]
result1 = sorted(array1, key=setting)
print(result1)
# [('바나나', 2), ('당근', 3), ('사과', 5)]
