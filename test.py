data = [10, 3, 11, 5, 9, 10]
# 1. 반복문을 활용하여 데이터를 순서대로 출력하시오

for i in range(len(data)):
    print(data)

# 2. 짝수만 출력하시오
for i in range(len(data)):
    if i % 2 == 0:
print(i)

# 3. 소수만 출력하시오 (소수는 자기 자신외에 나눠지지 않는 숫자 1제외)
def isprime(n):
    i = 2
    while i <= n:
        if n % i == 0: break
        i+=1
    if i == n:return True
    return False
print(isprime(10))
print(isprime(3))
print(isprime(11))
print(isprime(5))
print(isprime(9))
print(isprime(10))

# 이 부분 조금 헷갈려서 소수인지 아닌지 하나씩 판별했어요 ㅠㅠ 
# #한꺼번에 구하는 방법을 잘 모르겠어요 엉엉

students = [
    {"name": "시온", "age": 22, "score": {"수학": 80, "영어": 90, "국사": 100}},
    {"name": "효준", "age": 29, "score": {"수학": 100, "영어": 30, "국사": 30}},
    {"name": "승수", "age": 30, "score": {"수학": 10, "영어": 100, "국사": 100}},
    {"name": "창현", "age": 25, "score": {"수학": 100, "영어": 100, "국사": 100}},
]

# 4. 학생들의 나이 평균을 구하시오  

student_age = [22,29,30,25]
def average(student_age):
    sum = 0
    for i in range(len(student_age)):
        sum += list[i]
    
    return sum/len(student_age) 
print("평균값 : {}".format(average(student_age)))


# 5. 학생들의 수학점수 평균을 구하시오

list_math = [80,100,10,100] 

def average(list):
    count = 0
    for i in list:
        count += i
    return count/len(list)

print(average(list_math))

#  Q.리스트 자체에서 수를 빼서 평균구하는 법이 궁금해요!

# 6. 학생들의 과목별 평균을 구하시오 (.keys() 사용해서)
#     ex) student[i]['score'][key]

for student in students:
     if student['score']["수학"][0]: 
        student['score'] == sum['score'][0]/average['score'][0]
print(student)

for student in student:
     if student['score']["영어"][1]: 
        student['score'] == sum['score'][0]/average['score'][1]
print(student)

for student in student:
     if student['score']["국사"][2]: 
         student['score'] == sum['score'][0]/average['score'][2]
print(student)

# Q.이거 .. 잘 안돼요 ㅜㅜ


# 7. input() 활용하기
# 합이 100이 될때 까지 숫자 입력하기
result = 50
while result < 100:
    temp = int(input())
    result += temp
print(f"done result = {result}")

# Q. 계속 입력하는 건가요?

class_a_students = [
    {"name": "시온", "age": 22, "score": {"수학": 80, "영어": 90, "국사": 100}},
    {"name": "효준", "age": 29, "score": {"수학": 100, "영어": 30, "국사": 30}},
    {"name": "승수", "age": 30, "score": {"수학": 10, "영어": 100, "국사": 100}},
    {"name": "창현", "age": 25, "score": {"수학": 100, "영어": 100, "국사": 100}},
]

class_b_students = [
    {"name": "여진", "age": 29, "score": {"수학": 80, "영어": 90, "국사": 50}},
    {"name": "성찬", "age": 27, "score": {"수학": 100, "영어": 50, "국사": 80}},
    {"name": "다연", "age": 24, "score": {"수학": 100, "영어": 70, "국사": 80}},
    {"name": "윤상", "age": 40, "score": {"수학": 100, "영어": 100, "국사": 100}},
]

class_c_students = []  # 8명이 되어야함. append
# class_c_students.append(class_a_students[i])

# 8. A반과 B반의 토탈 성적 평균을 내시오 (각 과목별)
class_c_students = [ {"name": "시온", "age": 22, "score": {"수학": 80, "영어": 90, "국사": 100}},
    {"name": "효준", "age": 29, "score": {"수학": 100, "영어": 30, "국사": 30}},
    {"name": "승수", "age": 30, "score": {"수학": 10, "영어": 100, "국사": 100}},
    {"name": "창현", "age": 25, "score": {"수학": 100, "영어": 100, "국사": 100}}, 
    {"name": "여진", "age": 29, "score": {"수학": 80, "영어": 90, "국사": 50}},
    {"name": "성찬", "age": 27, "score": {"수학": 100, "영어": 50, "국사": 80}},
    {"name": "다연", "age": 24, "score": {"수학": 100, "영어": 70, "국사": 80}},
    {"name": "윤상", "age": 40, "score": {"수학": 100, "영어": 100, "국사": 100}},]

for student in students:
    if student["score"][0] == "수학":
        student['score'] == sum['score'][0]/average['score'][0]
print(students)

for student in students:
    if student["score"][1] == "영어":
        student['score'] == sum['score'][1]/average['score'][1]
print(students)

for student in students:
    if student["score"][2] == "국사":
        student['score'] == sum['score'][2]/average['score'][2]
print(students)

# Q.a,b반 다 합친 c를 만들었는데 ........뭐가 틀린건지 잘 모르겠어요ㅠㅠ

# 9. class_c_students라고 변수를 만들어서 a반과 b반의 학생들을 모두 넣으시오

class_c_students = [ {"name": "시온", "age": 22, "score": {"수학": 80, "영어": 90, "국사": 100}},
    {"name": "효준", "age": 29, "score": {"수학": 100, "영어": 30, "국사": 30}},
    {"name": "승수", "age": 30, "score": {"수학": 10, "영어": 100, "국사": 100}},
    {"name": "창현", "age": 25, "score": {"수학": 100, "영어": 100, "국사": 100}}, 
    {"name": "여진", "age": 29, "score": {"수학": 80, "영어": 90, "국사": 50}},
    {"name": "성찬", "age": 27, "score": {"수학": 100, "영어": 50, "국사": 80}},
    {"name": "다연", "age": 24, "score": {"수학": 100, "영어": 70, "국사": 80}},
    {"name": "윤상", "age": 40, "score": {"수학": 100, "영어": 100, "국사": 100}},]

# 10. MATRIX 복습 여기에 다시 짜보기 (외워서라도 괜찮으니 그냥 짜보기)

matrix_1 = [[1, 6], [4, 2]]
matrix_2 = [[3, 7], [3, 4]]
matrix_3 = [[0, 0], [0, 0]]
matrix_1[0][0] = matrix_1[0][0] + matrix_2[0][0]

for i in range(len(matrix_1)):
    for j in range(len(matrix_1[0])):  # len함수는 길이이므로 1개,2개,등 1부터 따진다. list는 0부터 따져서 마지막값 앞까지 온다.
        print(f"i={i} , j={j}")
        matrix_3[i][j] = matrix_1[i][j] + matrix_2[i][j]

print(matrix_3)


matrix_1 = [[4, 8, 2], [4, 5, 2]]
matrix_2 = [[8, 8, 0], [9, 7, 2]]
matrix_3 = [[0, 0, 0], [0, 0, 0]]

for i in range(len(matrix_1)):
    for j in range(len(matrix_1[0])):

        print(f"i={i} , j={j}")
        matrix_3[i][j] = matrix_1[i][j] + matrix_2[i][j]
print(matrix_3)
