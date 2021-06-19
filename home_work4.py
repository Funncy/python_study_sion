data = [
    {
        "name": "elie",
        "age": 28,
        "family": [
            {"name": "elie_father", "age": 58},
            {"name": "elie_mother", "age": 50},
            {"name": "elie_sister", "age": 30},
        ],
    },
    {
        "name": "teddy",
        "age": 31,
        "family": [
            {"name": "teddy_father", "age": 60},
            {"name": "teddy_mother", "age": 56},
        ],
    },
]

#컴퓨터는 바보임
#하나에 하나씩 밖에 못함
# 한줄씩밖에 못읽고
# 하나씩 밖에 접근 못함
# data에서 age를 가져오려면
# data=> 0번째 데이터 꺼내줘 => 거기서 age를 알려줘(key-value, map방식) (age 나옴)
# family의 age를 가져오려면
# data => 0번째 데이터 꺼내줘  (for로 반복) => 거기서 family 꺼내줘 => 거기서 0번째 꺼내줘 (for로 반복) => 거기서 age를 알려줘 (아빠 age나옴)
#  {
#        "name": "elie",
#        "age": 28,
#        "family": [
#            {"name": "elie_father", "age": 58},
#            {"name": "elie_mother", "age": 50},
#            {"name": "elie_sister", "age": 30},
#        ],
#    },
# data => 0번쨰 데이터 꺼내줘 => 1번째 데이터 꺼내줘  (age 나옴)
#    [
#      'elie',
#      28,
#       [ {"name": "elie_father", "age": 58},
#         {"name": "elie_mother", "age": 50},
#         {"name": "elie_sister", "age": 30},]
#    ]


# 데이터 구조에는 List, Map
# 둘다 여러개의 데이터를 넣는 자료구조 
# List는 여러개를 넣는거에 더 집중 , 번호를 붙여  (대괄호) []
list = ['sion','hyojon','arthur','sera','tyrion']

#List에서 자료를 꺼내려면 번호를 알려줘야함
list[0]
list[1]
# Map은 이름을 하나하나 붙여줌 (중괄호) {} key-value (key중복허용안함)
map = {
  'name' : 'sion',
  # 'name' : 'sion2', 중복 안됨 , 중복되면 누가 나올지 모름
  'name2' : 'hyojon',
  'name3' : 'arthur',
  'name4' : 'sera',
  'name5' : 'tyrion' 
}
#Map에서 자료를 꺼내려면 이름을 알려줘야 함
map['name']
map['name3']

data['age'] 
data[0]['age']
# data => 0번째에 무언가 있다, 그렇지만 무언가가 무엇인지는 알 수 없다.
# data[0] => 한 덩어리가 나올때 
# 그럴때는 data[0]['name']을 접근이 가능하다.

for i in data: 
  #i = 
  #{
  #      "name": "elie",
  #      "age": 28,
  #      "family": [
  #          {"name": "elie_father", "age": 58},
  #          {"name": "elie_mother", "age": 50},
  #          {"name": "elie_sister", "age": 30},
  #      ],
  #  },
  # ~~~중에서~ ~~을 뽑고 싶어요
  # 여러개가 있는데 (1개 일수도있지만) 그중에 내부에 있는 무언가를 꺼내고 싶어요
  # 반복문
  i['family']
  if data["family"] == "age":

data[0]["age"]
data[0]["family"][0]["age"]
data[0]["family"][1]["age"]
data[0]["family"][2]["age"]
data[1]["age"]
data[1]["family"][0]["age"]
data[1]["family"][1]["age"]

# 1. 내 이름 출력
# 2. 가족들 이름 출력

# 첫번째 문제
# 여기 있는 멤버들의 이름을 모두 출력해주세요.
# 일단 for문을 사용해서 \
# for i in range(len(data)): # 0


# 두번째 문제
# 여기 있는 멤버들의 나이를 모두 출력해주세요








i =  {
        "name": "elie",
        "age": 28,
        "family": [
            {"name": "elie_father", "age": 58},
            {"name": "elie_mother", "age": 50},
            {"name": "elie_sister", "age": 30},
        ],
    }

print(i['age'])






data = [
    {
        "name": "elie",
        "age": 28,
        "family": [
            {"name": "elie_father", "age": 58},
            {"name": "elie_mother", "age": 50},
            {"name": "elie_sister", "age": 30},
        ],
    },
    {
        "name": "teddy",
        "age": 31,
        "family": [
            {"name": "teddy_father", "age": 60},
            {"name": "teddy_mother", "age": 56},
        ],
    },
]
data[0]['family'][0]['age']
data[0]['family'][1]['age']
data[1]['family'][0]['age']
data[1]['family'][1]['age']

# family의 정보만 가져온 후에 
# age만 뽑는다.
# 리스트니깐 1번을 가지고 온다. 
# 그리고 2번째 있는 age를 뽑으려면 
# 
for i in data:
  print(i['age'])
  for j in i['family']:
    print(j['age'])


  


data = ['sion' , 'hyojun', 'arthur']


print(data[0])
print(data[1])

for i in data: # i = 'sion' 
  print(i)

for i in range(len(data)): # i = 0
  print(data[i])

# sion
# hyojun
# arthur

#  ['sion' , 'hyojun', 'arthur']
#  ['sion' , 'hyojun', 'arthur']
#  ['sion' , 'hyojun', 'arthur']


data = ['sion' , 'hyojun', 'arthur']

for i in data:
  print(i)

data = [
  {
  'name' : 'sion',
  'age' : 28
},
{
  'name' : 'hyojun',
  'age' : 30
},
{
  'name' : 'arthur',
  'age' : 12
}]

for i in data:
  print(i['name'])

for i in data:
  print(i['age'])

data  = [
  'sion' , 28 , 'hyojun' , 30, 'arthur' , 12
]

for i in data:
  print(i)

data = [
  ['sion' , 28],
  ['hyojun' , 30],
  ['arthur' , 12]
]

for i in data:
  print(i[0])

for i in data:
  print(i[1])

data = [
{
  'name' : 'sion',
  'age' : 28,
  'friends' : [
    'hyojun' , 'arthur'
  ]
},
{
  'name' : 'hyojun',
  'age' : 30,
  'friends' : [
    'hyojun' , 'arthur'
  ]
},
{
  'name' : 'arthur',
  'age' : 12,
  'friends' : [
    'hyojun' , 'arthur'
  ]
}
]

for i in data:
  print(i['friends'])  #  i['friends'] = [  'hyojun' , 'arthur' ]

for i in data: # i = 
  for j in i['friends']: # j = 'hyojun'
    print(j) 




data = [
{
  'name' : 'sion',
  'age' : 28,
  'friends' : [
    'hyojun' , 'arthur'
  ]
},
{
  'name' : 'hyojun',
  'age' : 30,
  'friends' : [
    'hyojun' , 'arthur'
  ]
},
{
  'name' : 'arthur',
  'age' : 12,
  'friends' : [
    'hyojun' , 'arthur'
  ]
}
]

# 모든 나이의 합을 구하시오 
# 모든 나이의 합을 구하는 과정을 출력하시오 
sum = 0
for i in data:
  print(i['age'])
  sum = sum + i['age']
  print(sum) # 28, 58, 70
print(sum)
# 70


