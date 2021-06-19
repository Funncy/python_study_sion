cell_members = [
    {
        "name": "효준",
        "age": 29,
        "sex": "남",
        "family": [
            {"name": "김서린", "age": 28, "sex": "여"},
            {"name": "임여진", "age": 29, "sex": "여"},
            {"name": "임재욱", "age": 26, "sex": "남"},
        ],
    },
    {
        "name": "시온",
        "age": 27,
        "sex": "여",
        "family": [
            {"name": "김헌철", "age": 62, "sex": "남"},
            {"name": "노명희", "age": 61, "sex": "여"},
            {"name": "김이레", "age": 31, "sex": "남"},
        ],
    },
]

# 숙제!!!!

# 1번문제. 셀원들 중 여자인 셀원들의 가족 구성원이 몇명인가요? !흰트 : (len() 사용) => print(len(~~))

# 1. 셀원들 중 여자인 셀원 한명씩 꺼낸다(for,if)
# 2. 꺼낸 데이터에서 가족데이터[family]를 한명씩 꺼낸다(for)
# 3. 꺼내진 가족데이터의 (len)을 출력한다.

for women in cell_members:
    if women["sex"] == "여":
        for my_family in women["family"]:
            print(my_family)
print(len(my_family))

# 2번문제. 셀원들의 가족멤버들 중에서  남자가 몇명인가요? (임시 변수를 쓰세요)

# 1. 셀원들의 가족들 데이터를 꺼낸다(for)
# 2. 가족들 데이터 중 "남자"인 가족의 데이터를 꺼낸다 (if = true)
# 3 .꺼내진 데이터가 참이면 임시변수(male)에 저장한다.
# 4. 임시변수(male)의 길이를 (len)함수를 이용하여 구한다.

male_number = {}

for i in cell_members:
    for male in i["family"]:
        if male["sex"] == "남":
            male_number = male
            print(male_number)
print(len(male_number))

# 3번문제. 셀원들의 가족 구성원 중 가장 나이가 많으신 분과 나이가 가장 어린 사람의 이름을 알려주세요. (각각) => 멤버가 3명이면 6명의 이름이 나와야함 (1명당 2명씩 이름 출력)
# ex. 시온이의 아버님과 시온이의 동생의 이름이 출력
# 효준이의 여동생과 효준이의 와이프 출력

# 이거 많이 헷갈려요..ㅜㅜ

#### 첫번째 "효준"의 경우
# 0. 변수들을 지정한다(가장 젊은, 가장 나이많은..)
# 1. 셀멤버들을 차례대로 하나씩 꺼낸다.(for)
# 2. 꺼내진 데이터중 데이터"이름(name)"이
#   "효준" 일때의 해당하는 가족데이터{family)만을 family_members에 하나씩 넣는다.[(if = true),(for)]
# 3. family_members의 "age"가 변수 old_age_1 보다 크거나 같으면 old_young_family에 family_members의 "이름"을 저장한다.
# 4. family_members의 "age"가 변수 young_age_1 보다 작거나 같으면 old_young_famaily에 family_members의 "이름"저장한다.
# 5. old_young_family를 프린트한다.

##### 두번째 "시온"의 경우
# 0. 변수들을 지정한다(가장 젊은, 가장 나이많은..)
# 1. 셀멤버들을 차례대로 하나씩 꺼낸다.(for)
# 2. 꺼내진 데이터중 데이터"이름(name)"이
#   "시온" 일때의 해당하는 가족데이터{family)만을 family_members에 하나씩 넣는다.[(if = true),(for)]
# 3. family_members의 "age"가 변수 old_age_2 보다 크거나 같으면 old_young_family에 family_members의 "이름"을 저장한다.
# 4. family_members의 "age"가 변수 young_age_2 보다 작거나 같으면 old_young_famaily에 family_members의 "이름"저장한다.
# 5. old_young_family를 프린트한다.


old_age_1 = 29
young_age_1 = 26
old_age_2 = 62
young_age_2 = 32

old_young_family = []

old_family_age = 0
old_family_name = ""
young_family_age = 9999
young_family_name = ""


# 0. 범용성 있는 코드
# 0-1. 기존 코드에서 if문 제거
for i in cell_members:
    for family_members in i["family"]:
        if family_members["age"] >= old_age_1:
            old_young_family = family_members["name"]
            print(old_young_family)
        elif family_members["age"] <= young_age_1:
            old_young_family = family_members["name"]
print(old_young_family)

# 0-2. 임시 변수 초기화 및 셀원별 데이터 출력
for i in cell_members:
    old_young_family = []  # 1.
    for family_members in i["family"]:
        if family_members["age"] >= old_age_1:
            old_young_family.append(family_members["name"])
            print(old_young_family)
        elif family_members["age"] <= young_age_1:
            old_young_family.append(family_members["name"])
    print(
        f'{i["name"]}의 가족 구성원중 나이가 가장 많으신 분과 나이가 가장 어리신 분은 다음과 같습니다. {old_young_family}'
    )  # 2.
    print(
        f'{i["name"]}의 가족 구성원중 나이가 가장 많으신 분과 나이가 가장 어리신 분은 다음과 같습니다. {old_young_family}'
    )

    #print(f'안녕{i['name']}하세요')
    #print(f'안녕{i["name"]}하세요')
    #print(f"안녕{i['name']}하세요")

# 0-3. 나이 임시 변수 설정
for i in cell_members:
    old_young_family = []
    old_family_age = 0
    young_family_age = 9999
    old_family_name = ""
    young_family_name = ""
    for family_members in i["family"]:
        if family_members["age"] >= old_family_age:
            old_family_name = family_members["name"]
            old_family_age = family_members["age"]
        elif family_members["age"] <= young_family_age:
            young_family_name = family_members["name"]
            young_family_age = family_members["age"]
    print(
        f'{i["name"]}의 가족 구성원중 나이가 가장 많으신 분 {old_family_name} , 나이가 가장 어리신 분 {young_family_name}'
    )  # 2.

# 1."효준"의 경우
for i in cell_members:
    if i["name"] == "효준":
        for family_members in i["family"]:
            if family_members["age"] >= old_age_1:
                old_young_family = family_members["name"]
                print(old_young_family)
            elif family_members["age"] <= young_age_1:
                old_young_family = family_members["name"]
print(old_young_family)

# 2."시온"의 경우
for i in cell_members:
    if i["name"] == "시온":
        for family_members in i["family"]:
            if family_members["age"] >= old_age_2:
                old_young_family = family_members["name"]
                print(old_young_family)
            elif family_members["age"] <= young_age_2:
                old_young_family = family_members["name"]
print(old_young_family)
