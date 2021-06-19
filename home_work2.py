data = [
    {"name": "시온", "grade": "2학년"},
    {"name": "창현", "grade": "1학년"},
    {"name": "승수", "grade": "1학년"},
    {"name": "성찬", "grade": "3학년"},
    {"name": "효준", "grade": "2학년"},
]

# 예시 (전체 학생 이름 출력
for student in data:
    print(student["name"])

# 다른 버전
for i in range(len(data)):
    print(data[i]["name"])

# 1번. 전체 학년(grade) 출력

# 2번. 내용을 맞춰보시오
for i in range(len(data)):
    if data[i]["name"] == "시온":
        print(data[i]["grade"])

# 3번. 내용을 맞춰보시오
for student in data:
    if student["grade"] == "2학년":
        print(student)

# 4번. 1학년 학생들 이름 출력
# 아래와 같이 나오게 작성
# 창현
# 승수
