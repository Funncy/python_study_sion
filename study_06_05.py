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


# 2번 멤버들의 가족중 나이가 가장 많은 사람 1분을 출력해주세요.

# 0. 가장 큰 나이를 확인하기 위한 기준값 Max_age에 0을 넣은다.
# 1. 데이터 덩어리 (멤버목록)에서 하나씩 꺼낸다.
# 1-1. 꺼낸 데이터 (1명의 개인 데이터)에서 가족들 데이터를 꺼낸다.
# 1-2. 가족들 데이터 (여러명일 수 있음, 1명일수도 없을 수도 있음)에서 한명씩 꺼낸다.
# 1-2-1. 한명씩 꺼낸 가족 데이터 (1명의 개인 데이터)에서 나이를 꺼낸다.
# 1-2-2. max_age(기준값, 가장 높은값인지 확인하기 위한)보다 꺼낸 가족 데이터가 더 큰 값인지 확인한다. (if 들여쓰기 들어가야함)
# 1-2-3. 가족의 나이가 max_age보다 더 크다면 max_age를 교체한다.
# 2. max_age를 출력한다.

# 1번 방법 : 임시 변수에 기록 한다. ﹖
# 2번 방법 : 데이터를 저장한다. ✨
# 3번 방법 : 데이터 위치를 저장한다. 💩

max_age = 0
max_name = ""
max_member_index = 0
max_family_index = 0
for i in cell_members:
    for j in i["family"]:
        print(f"나이 비교중 현재 max_age = {max_age} , 가족 나이 = {j['age']}")
        if max_age < j["age"]:
            max_age = j["age"]
            max_name = j["name"]
            max_member = j
            print(f"교체 완료 ... max_age => {max_age}")
print(max_age)
print(max_name)
print(max_member["name"])
print(cell_members[max_member_index]["family"][max_family_index]["name"])


# 3번 셀원들중 30살 이하의 셀원의 가족들중 남자이면서 30살 이하인 사람을 출력해주세요
# 셀원들 중 30살 이하
# 그 셀원의 가족들중 30살 이하
# 그 사람의 이름


# 0. 30살 이하인 사람들 확인하기 위해 기준값인 avg_age에 30을 넣는다
# 1. 데이터 덩어리(멤버목록)에서 하나씩 꺼낸다.
# 1-1. 꺼낸 데이터에서 가족들 데이터를 꺼낸다
# 1-2. 꺼낸 가족들 데이터중 성별이 남자인 데이터를 꺼낸다 => 남자 인지 확인한다.
# 1-3 성별이 남자인 데이터중 avg_age(30)보다 작은 값인지 확인
# 1-4. 가족의 나이가 avg_age보다 작다면 avg_age(30)를 교체한다
# 2. avg_age를 출력한다

# 셀원 나이 확인 30살 이하인지


avg_age = 35

for me in cell_members:
    for family in me["family"]:
        if family["sex"] == "남":
            if avg_age > family["age"]:
                avg_age = family["age"]
print(avg_age)

# 0. 기준값 standard_age = 30
# 1.  셀원들 목록에서 셀원 한명씩 꺼낸다. (for)
# 1-1. 꺼낸 셀원의 나이가 standard_age보다 작은 사람만 다음 조건을 실행한다. (if) == true
# 1-1-1. 꺼낸 셀원 데이터 에서 셀원의 가족들 데이터를 꺼낸다. (for)
# 1-1-1-2. 꺼낸 셀원의 가족에서 (1명의 데이터) 성별이 남자인 사람만 다음 조건을 실행한다. (if) == true
# 1-1-1-2-1. 그 셀원 가족의 나이가 standard_age 보다 작은 사람만 다음 조건을 실행한다. (if) == true
# 1-1-1-2-1-1. 그 셀원 가족의 이름을 출력한다. (print)

standard_age = 30
for cell_member in cell_members:
    if cell_member["age"] < standard_age:
        for member_family in cell_member["family"]:
            if member_family["family"] == "남":
                if member_family["age"] < standard_age:
                    print(member_family["name"])


# 3번 셀원들중 가족 구성원의 숫자가 2명 이상인 사람(셀원)의 나이를 출력하세요.
# 1. 셀원들 목록에서 셀원 한명씩 꺼낸다 (for)
# 2. 꺼낸 셀원데이터중 가족데이터[family]를 꺼낸다 (for) => 한명 한명을 보겠다 💩
# 3.꺼낸 가족들 데이터중 data_list(len)가 3 이상인 사람만 다음 조건을 실행한다(if) == True
# 4.  그 셀원의 나이를 출력한다 (print)

for cell_member in cell_members:
    for member_family in cell_member["family"]:
        if len(cell_member["family"]) > 1:
            print(cell_member["age"])
print("-------------------------------------------")
for cell_member in cell_members:
    if len(cell_member["family"]) > 1:
        print(cell_member["age"])


# 숙제!!!!

# 1번 셀원들 중 여자인 셀원들의 가족 구성원이 몇명인가요? !흰트 : (len() 사용) => print(len(~~))

# 2번 셀원들의 가족멤버들 중에서  남자가 몇명인가요? (임시 변수를 쓰세요)

# 3번 셀원들의 가족 구성원 중 가장 나이가 많으신 분과 나이가 가장 어린 사람의 이름을 알려주세요. (각각) => 멤버가 3명이면 6명의 이름이 나와야함 (1명당 2명씩 이름 출력)
# ex. 시온이의 아버님과 시온이의 동생의 이름이 출력
# 효준이의 여동생과 효준이의 와이프 출력
