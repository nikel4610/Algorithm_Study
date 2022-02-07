# 각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생 이름 출력 프로그램 작성
# 첫번째 줄에 학생의 수 N이 입력된다
# 두번째 줄 부터 학생의 이름 문자열A 와 성적을 나타내는 정수B가 공백으로 구분되어 입력된다

n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    # 이름은 문자열 그대로, 점수는 정수형으로 변환 후 저장
    array.append((input_data[0], int(input_data[1])))

# 키를 이용하여 점수를 기준으로 정렬
array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')

# 2
# 홍길동 95
# 이순신 77
# 이순신 홍길동 
