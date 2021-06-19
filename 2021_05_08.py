data = [
    {"name": "시온", "grade": "2학년"},
    {"name": "창현", "grade": "1학년"},
    {"name": "승수", "grade": "1학년"},
    {"name": "성찬", "grade": "3학년"},
    {"name": "효준", "grade": "2학년"},
]

data = [1, 10, 8, 9, 7]


students = [
    {
        "name": "시온",
        "grade": "2학년",
        "subjects": [
            {"name": "수학", "score": 80, "담임샘": "효준"},
            {"name": "영어", "score": 78, "담임샘": "승수"},
            {"name": "국어", "score": 90, "담임샘": "창현"},
        ],
    },
    {
        "name": "시온 동생",
        "grade": "1학년",
        "subjects": [
            {"name": "수학", "score": 80, "담임샘": "창현"},
            {"name": "영어", "score": 78, "담임샘": "승수"},
            {"name": "국어", "score": 90, "담임샘": "효준"},
        ],
    },
]
# 고민이 중요함
# 정답이 중요한게 아님
# 1. 학생 수학 점수 평균 내주세요

# 2. 효준 선생님이 가르친 과목의 평균을 내주세요

# 3. 효준 선생님이 가르치고 있는 과목을 알려주세요 (여러개 일 수 있음)

library_books = [
    {
        "code": 1002,
        "name": "python 정석",
        "published": "2021-05-08",
        "arthor": "김효준",
    },
    {
        "code": 1003,  # key값 => 중복 불가 => 고유한 번호
        "name": "영어의 정석",
        "published": "2019-05-08",
        "arthor": "김시온",
    },
    {
        "code": 1004,
        "name": "Html 정석",
        "published": "2021-05-08",
        "arthor": "이창현",
    },
]

sion_books = []

while 1:
    print("--------------")
    print(" 도서관 프로그램")
    print(" 1. 도서 목록 확인")
    print(" 2. 도서 대여 목록 확인")
    print(" 3. 도서 대여")
    print(" 4. 도서 반납")
    print(" 0. 종료")
    print(" 키를 입력해주세요.")
    print("--------------")

    key = input()
    if key == "0":
        break
    elif key == "1":
        # 도서 목록 출력
        print("도서 목록 출력 화면 입니다")
        # for book in library_books:
        #     print(f' 책 이름 : {book["name"]} 책 저자 : {book["arthor"]}')
        # 단점, 몇번째 책인지 알려줄수 없음
        for i in range(len(library_books)):
            print("-------------------------")
            print(f' {i+1}번  책 이름 : {library_books[i]["name"]}')
            print(f' 책 코드 : {library_books[i]["code"]}')
            print("-------------------------")
    elif key == "2":
        # 도서 대여 목록 확인
        print("당신이 대여한 책 목록은 다음과 같습니다")
        for i in range(len(sion_books)):
            print("-------------------------")
            print(f' {i+1}번  책 이름 : {sion_books[i]["name"]}')
            print(f' 책 코드 : {sion_books[i]["code"]}')
            print("-------------------------")
    elif key == "3":
        # 도서 대여
        print("대여하고자 하시는 도서의 번호를 입력해주세요")
        book_code = int(input())
        is_find = False
        for book in library_books:
            if book["code"] == book_code:
                # 내 대여 목록 추가
                sion_books.append(book)
                # 도서관 책목록에서 삭제
                library_books.remove(book)
                # 책 찾기 완료
                is_find = True
                # 반복 횟수 줄이기
                break
        # 없으면 잘못된 코드입니다.
        if is_find == False:
            print("잘못된 책 번호입니다.")
    elif key == "4":
        # 도서 반납
        print("반납하고자 하시는 도서의 번호를 입력해주세요")
        book_code = int(input())
        is_find = False
        for book in sion_books:
            if book["code"] == book_code:
                # 도서관 책 목록 추가
                library_books.append(book)
                # 내 대여 목록 삭제
                sion_books.remove(book)
                # 책 찾기 완료
                is_find = True
                # 반복 횟수 줄이기
                break
        # 없으면 잘못된 코드입니다.
        if is_find == False:
            print("잘못된 책 번호입니다.")
    else:
        print("잘못된 번호를 입력하셨습니다")


print("프로그램이 종료되었습니다")
