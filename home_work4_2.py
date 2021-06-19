# 1번
# 화면에 위 문장을 하나씩 출력하시오
data = ["파이썬", "재미있어", "하지만", "어려워"]


# 2번
# 화면에 위 문장을 하나씩 출력하시오
data = {"first": "파이썬", "second": "재미있어", "third": "하지만", "fourth": "어려워"}

for i in data.values():  # map의 특징
    print(i)

# 3번
# 이름을 모두 출력해주세요 (하나씩)
data = {
    "names": ["효준", "시온", "승수"],
    "ages": [29, 25, 30],
    "height": [173, 168, 180],
}
# for i in data: 로 시작안함 조금 다름 아주 조금
# for ㅑ in in data['~~~']:

# 4번
# 이름을 모두 출력해주세요 (하나씩)
data = [
    ["효준", "시온", "승수"],
    [29, 25, 30],
    [173, 168, 180],
]
# for i in data: 로 시작안함 조금 다름 아주 조금
# for in in data[숫자]:

# 5번
# 나이를 모두 더해주세요
data = {
    "names": ["효준", "시온", "승수"],
    "ages": [29, 25, 30],
    "height": [173, 168, 180],
}  # for i in data: 로 시작안함 조금 다름 아주 조금
# for ㅑ in in data['~~~']:

# 6번
# 이름을 모두 출력해주세요
data = [
    {"name": "시온"},
    {"name": "효준"},
    {"name": "승수"},
]

# 7번
# 나이를 모두 더해주세요
data = [
    {"name": "시온", "age": 25},
    {"name": "효준", "age": 30},
    {"name": "승수", "age": 32},
]

# 8번
# 각자의 친구들을(이름) 모두 출력하시오
data = [
    {"name": "시온", "age": 26, "friends": ["hyojun", "arthur"]},
    {"name": "효준", "age": 30, "friends": ["arthur"]},
    {
        "name": "승수",
        "age": 21,
        "friends": [
            "hyojun",
        ],
    },
]

# 9번
# 각자의 친구들을(이름) 모두 출력하시오
data = [
    {
        "name": "시온",
        "age": 26,
        "friends": [
            {"name": "hyojun"},
            {"name": "arthur"},
        ],
    },
    {
        "name": "효준",
        "age": 30,
        "friends": [
            {"name": "arthur"},
        ],
    },
    {
        "name": "승수",
        "age": 21,
        "friends": [
            {"name": "hyojun"},
        ],
    },
]

# 10번
# 각자 친구들 나이를 출력하시오
data = [
    {
        "name": "시온",
        "age": 26,
        "friends": [
            {"name": "hyojun", "age": 28},
            {"name": "arthur", "age": 28},
        ],
    },
    {
        "name": "효준",
        "age": 30,
        "friends": [
            {"name": "arthur", "age": 28},
        ],
    },
    {
        "name": "승수",
        "age": 21,
        "friends": [
            {"name": "hyojun", "age": 28},
        ],
    },
]
