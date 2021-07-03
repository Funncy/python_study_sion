student_list = [
    {
        "이름": "시온",
        "학년": "2학년",
        "학교": {"이름": "꿈의대학", "설립연도": 1998, "주소": "꿈의 대학 주소 ~~"},
        "수강과목": [
            {"이름": "수학", "점수": 80},
            {"이름": "영어", "점수": 70},
            {"이름": "국어", "점수": 100},
        ],
    },
    {
        "이름": "효준",
        "학년": "3학년",
        "학교": {"이름": "꿈의대학", "설립연도": 1998, "주소": "꿈의 대학 주소 ~~"},
        "수강과목": [
            {"이름": "수학", "점수": 80},
            {"이름": "영어", "점수": 100},
            {"이름": "국어", "점수": 80},
        ],
    },
    {
        "이름": "승수",
        "학년": "1학년",
        "학교": {"이름": "꿈의대학원", "설립연도": 2002, "주소": "꿈의 대학원 주소 ~~"},
        "수강과목": [
            {"이름": "수학", "점수": 70},
            {"이름": "영어", "점수": 70},
            {"이름": "국어", "점수": 70},
        ],
    },
]

# 1. 결과를 맞춰보시오
for student in student_list:
    total = 0
    for subject in student["수강과목"]:
        total += subject["점수"]  # total = total + subject['점수']와 같은 의미
    avg = total / len(subject)  # len(subject)는 subject 리스트의 길이

    for subject in student["수강과목"]:
        if avg <= subject["점수"]:
            print(f"{student['이름']}의 {subject['이름']}은 평균 이상입니다.")


# 2. 결과를 맞춰보시오
total = 0
subject_len = 0
for student in student_list:
    for subject in student["수강과목"]:
        total += subject["점수"]
    subject_len += len(subject)

avg = total / subject_len

for student in student_list:
    for subject in student["수강과목"]:
        if subject["점수"] >= avg:
            print(f"{student['이름']}의 {subject['이름']}은 평균 이상입니다.")

# 3. 1번과 2번의 차이는 무엇인가요? 둘다 평균 이상 점수를 찾는 로직인데 무엇이 다른가요?
