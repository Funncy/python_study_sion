data = [10, 3, 11, 5, 9, 10, 11, 12]


print(len(data))  # 8
# 배열의 순서대로 숫자를 출력
# 배열의 갯수를 0~N-1까지 i에 담긴다
# index 즉 번호를 넘겨주는 방식
# data[i]
# for i in range(len(data)):  # range(8) 0~7
#     print(data[i])  # data[0] data[1] data[2]....

# 직접 값 접근
for i in data:
    print(f"number = {i}")

# 배열에 값을 순서대로 조회하는 방식은 크게 2가지
# 1. index 접근 법
# for i in range(len(data)):
#   print(data[i])
# 2. 직접 값 접근 법
# for i in data:
#   print(i)


# 1. 정의
# 2. 조건
# 3. 마무리 연산
int i = 0;
while(i<3) {

  i++;
}
for(int i=0; i<3; i++) {

}

#반복문은 조건문이 합쳐져 있는 형태다
#어떤 조건이 True인 동안 반복해라~

bool isSuccess = false;
while(isSuccess == false) {
  if(sion.getWhileConcept() == true) {
    isSuccess = true;
  }
}

List<String> students = ['효준', '성찬', '승수', '창현', '시온'];
int number = 0;
while(students[number] != '시온') {
  print(students[number])
  number++;
}

for(int number=0; students[number] != '시온' ; number++) {
  print(students[number])
}

# 모든 반복문은 탈출구가 있어야한다 
# 없을시 무한루프에 빠져 프로그램이 멈춘다
# 일부러 무한루프에 넣는 경우도 있음 
# 이런 경우도 탈출구 
# Ex. 게임 => 종료 버튼을 눌러야만 게임미 종료 아니면 계속 돌아감

List<int> data = [10,23,11,11,223,512];
for(int i=0; i<len(data); i++){
  print(data[i])
}

data = [
  {
    'name' : '시온',
    'scores' : {
      '수학' : 80,
      '영어' : 100,
      '프로그래밍' : 99,
      '국어' : 60,
    }
  },
  ....
]

for student in data
  print(student['scores']['수학'])

#직접 접근 방식
for i in data:
  print(i)

#index방식
for i in range(len(data)):
  print(data[i])

#index 조건으로 돌면서
# 출력은 직접 출력방식 (dataX)
# (index) => index출력
for i in range(len(data)):
  print(i)




print(i)

in => 안에~
for i in data:
for i in range(10):


for i in range(len(data)):
  print(i)
print(i)