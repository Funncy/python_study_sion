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


def print_books(books):
    for i in range(len(books)):
        print("-------------------------")
        print(f' {i+1}번  책 이름 : {books[i]["name"]}')
        print(f' 책 코드 : {books[i]["code"]}')
        print("-------------------------")


def swap_book(main_books, sub_books):
    book_code = int(input())
    is_find = False
    for book in main_books:
        if book["code"] == book_code:
            # 도서관 책 목록 추가
            sub_books.append(book)
            # 내 대여 목록 삭제
            main_books.remove(book)
            # 책 찾기 완료
            is_find = True
            # 반복 횟수 줄이기
            break
        # 없으면 잘못된 코드입니다.
        if is_find == False:
            print("잘못된 책 번호입니다.")


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
        print_books(library_books)
    elif key == "2":
        # 도서 대여 목록 확인
        print("당신이 대여한 책 목록은 다음과 같습니다")
        print_books(sion_books)
    elif key == "3":
        # 도서 대여
        print("대여하고자 하시는 도서의 번호를 입력해주세요")
        swap_book(library_books, sion_books)
    elif key == "4":
        # 도서 반납
        print("반납하고자 하시는 도서의 번호를 입력해주세요")
        swap_book(sion_books, library_books)
    else:
        print("잘못된 번호를 입력하셨습니다")


print("프로그램이 종료되었습니다")
