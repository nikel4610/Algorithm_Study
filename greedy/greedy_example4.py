# 1이 될 때 까지
# 어떤 수 N이 1이 될 때까지 다음 두 과정중 하나를 반복하여 선택 수행
# 1. N-1
# 2. N/K
# N이 1이 될 때까지 수행해야 하는 최소 과정 횟수 구하기

n, k = map(int, input().split())
result = 0

# while n >= k: # N이 K 이상일 때 K로 계속 나누기
#     while n % k != 0: # 나머지가 0이 아닐때
#         n -= 1 # N-1 수행
#         result += 1
#     n //= k # K로 나누기
#     result += 1
# while n > 1: # 마지막 남은 수에 대해 1씩 빼기
#     n -= 1
#     result += 1
   
while True:
    # n k로 나누어 떨어지는 수가 될 떄까지 1씩 빼기
    target = (n // k) * k
    result += ( n - target )
    n = target
    
    # k로 나눌 수 없을 때 break
    if n < k:
        break
    result += 1
    n //= k
    
result += (n - 1) # 마지막으로 남은 수에 대해 1씩 빼기
print(result) # 25 5 -> result = 2
