  {
        "이름": "승수",
        "학년": "1학년",
        "학교": {"이름": "꿈의대학원", "설립연도": 2002, "주소": "꿈의 대학원 주소 ~~"},
        "수강과목": [
            {"이름": "수학", "점수": 70},
             {"이름": "수학", "점수": 70},
              {"이름": "수학", "점수": 80},
               {"이름": "수학", "점수": 90},
                {"이름": "수학", "점수": 90},
        ],
    },

for student in student_list:
    max_subjcet_score = 90
    max_subject = []

    for subject in student["수강과목"]:
        # 1. 최고 점수보다 크다 => 최고값 갱신
        # 2. 최고 점수보다 작다 => 무시
        # 3. 최고 점수랑 같다 => 쌓는다
        if subject["점수"] > max_subjcet_score:
            max_subjcet_score = subject["점수"]
            max_subject.clear()
            max_subject.append(subject)

        elif subject["점수"] == max_subjcet_score:
            max_subject.append(subject)

    for subject in max_subject:
        print(f'{student["이름"]}의 {subject["이름"]}의 점수는 {subject["점수"]}입니다.')

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

[1, 2, 3]
{
    "1": 2,
    "2": 3,
}

# 1.
for student in student_list:
    if student["학교"]["이름"] == "꿈의대학":
        for subject in student["수강과목"]:
            print(f'{student["이름"]}의 {subject["이름"]} 점수 : {subject["점수"]}')

# 1. student_list를 student안으로 순환. =>
# 2. student 리스트 중 "학교" 안의 "이름"들이 "꿈의대학" 이라면
# 3. student 리스트 안의 "수강과목"을 subject 안으로 순환
# 4. 따라서
# 시온의 수학 점수:80
# 시온의 영어 점수:70
# 시온의 국어 점수:100
# 효준의 수학 점수:80
# 효준의 수학 점수:100
# 효준의 국어 점수:80
# 5 승수는 "꿈의 대학원"이기 때문에 순환하지 않는다.


# 2.

for student in student_list:
    max_subjcet_score = 0
    max_subject = []

    for subject in student["수강과목"]:
        if subject["점수"] > max_subjcet_score:
            max_subjcet_score = subject["점수"]
            max_subject.clear()
            max_subject.append(subject)

    for subject in max_subject:
        print(f'{student["이름"]}의 {subject["이름"]}의 점수는 {subject["점수"]}입니다.')

for student in student_list:
    max_subjcet_score = 0
    max_subject_name = ""
    for subject in student["수강과목"]:

        if subject["점수"] >= max_subjcet_score:
            max_subjcet_score = subject["점수"]
            max_subject_name = subject["이름"]
    print(f'{student["이름"]}의 {max_subject_name}의 점수는 {max_subjcet_score}입니다.')

# 1. student_list를 student로 순환시킨다.
# 2. 중간에 최대 과목 점수와 이름의 임시변수를 지정해 주었음. (임시변수 = 기준값)
# 3. student의 "수강과목"을 subject로 순환시킨다.
# 4. 순환하는 subject의 점수가 0보다 크거나 같다면

# subject"점수"를 max_subject_score로 대입시킨다.
# subject"이름"을 max_subject_name으로 대입시킨다.
#  시온은 80 70 100 중 가장 큰 100으로 max_subject_score와 max_subject_name으로 대입된다.
#  효준은 80 100 80 중 가장 높은 값인 100에서 멈추므로 100점에서 max_subject_socre와 max_subject_name
# 으로 대입된다.
# 승수는 70 70 70 중 가장 큰 70이므로 다른 값으로 변하지 않고 첫번째 70으로 대입된다.
# 따라서
# 시온의 국어의 점수는 100 입니다.
# 효준의 영어의 점수는 100 입니다.
# 승수의 국어의 점수는 70입니다.


# 3.
for student in student_list:
    total = 0
    for subject in student["수강과목"]:
        total = total + subject["점수"]
    if total > 250:
        print(f'{student["이름"]}은 우수생입니다.')
    elif total > 200:
        print(f'{student["이름"]}은 잘하고 있습니다.')
    else:
        print(f'{student["이름"]}은 조금 분발해야합니다.')

# 1. student_list를 student안으로 순환
# total 변수를 0으로 지정
# 2. student"수강과목"을 subject안으로 순환
# total + subject["점수"]를 total로 대입
# "시온"의경우
# 80=0+80        total:80
# 150=80 + 70     total:150
# 250=150+100     total:250

# "효준"의 경우
# 80=0+80        total:80
# 180=80+100     total:180
# 280=180+100    total:280

# "승수"의 경우
# 70=0+70        total:70
# 140=70+70      total:140
# 210=140+70     total:210

# 따라서
# 시온은 잘하고 있습니다.            (250)
# 효준은 우수생입니다.               (280)
# 승수는 잘하고 있습니다.            (210)


# 4. 인문대학원 권유
for student in student_list:
    if student["학교"]["이름"] == "꿈의대학":
        total = 0
        for subject in student["수강과목"]:
            if subject["name"] != "수학":
                total = total + subject["점수"]
        if total > 150:
            print(f'{student["이름"]}학생 대학원을 생각해보지 않겠나?')


# 1. student_list를 student로 순환
# 2. student의 "학교"중 "이름"이 "꿈의대학"이라면 total = 0
# 3. student"수강과목"을 subject로 순환
# 4. subject의 "name"이 "수학"이 아니라면 total+subject"점수"를 total로 대입
# "시온"의 경우
# 70=0+70       total:70
# 170=70+100    total:170


# "효준"의 경우
# 100=100+0       total:100
# 180=100+80     total:180


# "승수"의 경우
# 70=0+70        total:70
# 140=70+70      total:140


# 5. total>150 이라면

# 따라서
# 효준학생 대학원을 생각해보지 않겠나?  >>지당하십니다 :)
