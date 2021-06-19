data = [
    {
        "name": "시온",
        "subjects": [
            {"name": "수학", "score": 80},
            {"name": "영어", "score": 70},
            {"name": "국어", "score": 90},
            {"name": "파이썬", "score": 100},
        ],
        "grade": "2학년",
    },
    {
        "name": "창현",
        "subjects": [
            {"name": "수학", "score": 70},
            {"name": "영어", "score": 100},
            {"name": "국어", "score": 80},
            {"name": "파이썬", "score": 80},
        ],
        "grade": "2학년",
    },
    {
        "name": "승수",
        "subjects": [
            {"name": "수학", "score": 69},
            {"name": "영어", "score": 100},
            {"name": "국어", "score": 100},
            {"name": "파이썬", "score": 60},
        ],
        "grade": "2학년",
    },
    {
        "name": "효준",
        "subjects": [
            {"name": "수학", "score": 90},
            {"name": "영어", "score": 60},
            {"name": "국어", "score": 50},
            {"name": "파이썬", "score": 100},
        ],
        "grade": "3학년",
    },
    {
        "name": "성찬",
        "subjects": [
            {"name": "수학", "score": 100},
            {"name": "영어", "score": 30},
            {"name": "국어", "score": 20},
            {"name": "파이썬", "score": 100},
        ],
        "grade": "3학년",
    },
]

# 예시 (전체 학생 학년 출력)
for student in data:
    print(student["grade"])

# 1번 전체 학급 학생 이름을 출력하시오.
