# 팩토리얼 예제
# 반복적으로 구현한 n!
def functional_iterative(n):
    result = 1
    # 1에서부터 n까지 수를 차례로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

print('반복적으로 구현: ', functional_iterative(5))
print('재귀적으로 구현: ', factorial_recursive(5))
# 반복적으로 구현:  120
# 재귀적으로 구현:  120
