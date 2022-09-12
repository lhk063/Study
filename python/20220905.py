# print("hellow world")

# 숫자 출력
# print(5)
# print(-10)
# print(3.14)
# print(1000)

# 연산
# print(5+3)
# print(2*8)
# print(3*(3+1))

# 문자열
# print('풍선')
# print("풍선")
# print("바니"*4)
# print("당근"*2)

# boolean 불리안 : 참과 거짓을 의미
# print(5 > 10) # result : false
# print(5 < 10) # result : true
# print(True) # result : true
# print(False) # result : false
# print(not True) # result : false
# print(not False) # result : true
# print(not (5 > 10)) # result : true

# # 변수
# animal = "강아지"
# name = "연탄이"
# age = 4
# hobby = "산책"
# is_adult = age >= 3
# print("우리집" + animal + "의 이름은" + name + "이에요")
# print(name + "는" + str(age) + "살이며," + hobby + "을 아주 좋아해요")
# print(name + "는 어른일까요?" + str(is_adult))

# # practice 1
# station = "사당"
# station = "신도림"
# station = "인천공항"
# print(station + "행 열차가 들어오고 있습니니다")

# # 연산자
# print(1 + 1)
# print(3 - 2)
# print(5 * 2)
# print(6 / 3)

# print(2 ** 3)  # 제곱
# print(5 % 3)  # 나머지
# print(10 % 3)
# print(5//3)  # 몫
# print(10//3)

# print(10 > 3)
# print(4 >= 7)
# print(10 < 3)
# print(5 <= 5)

# print(3 == 3)  # 같다
# print(4 == 2)
# print(3 + 4 == 7)

# print(1 != 3)  # 같지 않다
# print(not (1 != 3))

# print((3 > 0) and (3 < 5))  # true
# print((3 > 0) & (3 < 5))  # true

# print((3 > 0) or (3 > 5))  # true
# print((3 > 0) | (3 > 5))  # true

# print(5 > 4 > 3) # true
# print(5 > 4 > 7) # false


# print(2 + 3 * 4)
# print((2 + 3) * 4)
# number = 2 + 3 * 4  # 14
# print(number)
# number = number + 2
# print(number)
# number += 2
# print(number)
# number *= 2
# print(number)
# number /= 2
# print(number)
# number -= 2
# print(number)

# number %= 5
# print(number)


# from math import *
# print(abs(-5))
# print(pow(4, 2))  # 4^2 = 4*4 = 16
# print(max(5, 12))  # 12
# print(min(5, 12))  # 5
# print(round(3.14))  # 반올림
# print(round(4.99))

# print(floor(4.99))  # 내림
# print(ceil(3.14))  # 올림
# print(sqrt(16)) # 제곱근 출력

# 랜덤함수
# from random import *
# print(random())  # 0.0 ~ 1.0 미만의 임의의 값 생성
# print(random() * 10)
# print(int(random() * 10))
# print(int(random() * 10) + 1)

# print(int(random() * 45) + 1)
# print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성

# practice 2
# from random import *
# date = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월"+str(date)+"일로 선정되었습니다?")

# # 문자열
# sentence = "나는 소년입니다"
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요.
# """
# print(sentence3)

# # 슬라이싱
# register_address = "941225-1234567"
# print("성별 : " + register_address[7])
# print("연 : " + register_address[0:2])  # 0 ~ 2 직전까지
# print("월 : " + register_address[2:4])
# print("일 : " + register_address[4:6])
# print("생년월일 : " + register_address[:6])
# print("뒷 자리 : " + register_address[7:])
# print("뒤 7자리 (뒤에서부터) : " + register_address[-7:])

# # 문자열 처리 함수
# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)

# print(python.find("Java"))  # 값을 못찾을때 -1 출력 후 계속 진행
# # print(python.index("Java")) # 값을 못찾을때 오류 출력 후 멈춤

# print(python.count("n"))

# print("a" + "b")
# print("a", "b")


# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아해요." % "파이썬")
# print("Apple 은 %c로 시작해요" % "A")
# print("나는 %s색과 %s색을 좋아해요." % ("파랑", "빨강"))
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파랑", "빨강"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파랑", "빨강"))

# print("나는{age}살이며, {color}색을 좋아해요".format(age=20, color="red"))

# age = 29
# color = "blue"
# print(f"나는{age}살이며, {color}색을 좋아해요")


# # 탈출 문자

# # \n : 줄바꿈
# print("백문이 불여일견 \n백견이 불여일타")

# # \"\' : 문장 내에서 따옴표
# # 저는 "나도코딩"입니다.
# print("저는 '나도코딩'입니다.")
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.")

# # \\ : 문장 내에서 \
# print("\\a\\b\\c")

# # \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")

# # \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")

# # \t : 탭
# print("Red\tApple")

# # practice3
# url = "http://naver.com"
# slice_url = url.replace("http://", "")
# print(slice_url)
# slice_url = slice_url[:slice_url.index(".")]
# print(slice_url)
# password = slice_url[:3] + str(len(slice_url)) + str(slice_url.count("e")) + "!"
# print(f"비밀번호는 {password}입니다.")


# 리스트 []
# 지하철 칸별로 10,20,30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)
# subway = ["유재석", "조세호", "박명수"]
# print(subway)
# print(subway.index("조세호"))

# subway.append("하하")
# print(subway)

# subway.insert(1, "정형돈")
# print(subway)

# print(subway.pop)
# print(subway)

# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# # 숫자 정렬
# num = [5, 2, 3, 4, 1]
# num.sort()
# print(num)

# num.reverse()
# print(num)

# num.clear()
# print(num)

# mix = ["조세호", 20, True]
# print(mix)

# num.extend(mix)
# print(num)


# # dic
# dic = {3: "유재석", 100: "김태호"}
# print(dic[3])
# print(dic[100])

# print(dic.get(3))
# # print(dic[5])
# print(dic.get(5))  # 값이 없는 경우에 none 출력후 이어나갈 수 있다.
# print("hi")

# print(3 in dic)  # key 있는지 확인 여부 있으면 true
# print(5 in dic)

# # add
# print(dic)
# dic["c-20"] = "조세호"
# dic[3] = "김종국"
# print(dic)

# # delete
# del dic[3]
# print(dic)

# # print key
# print(dic.keys())
# # print value
# print(dic.values())
# # print key/values
# print(dic.items())
# # clear
# dic.clear()
# print(dic)


# # tuple
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])
# # menu.add 튜플은 추가가 불가하다.

# name, age, hobby = ("김종국", 20, "코딩")
# print(name, age, hobby)


# # 집합 set
# # 중복 안됨, 순서 없음
# my_Set = {1, 2, 3, 3, 3}
# print(my_Set)
# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# # 교집합
# print(java & python)
# print(java.intersection(python))

# # 합집합
# print(java | python)
# print(java.union(python))

# # 차집합
# print(java - python)
# print(java.difference(python))

# # add
# python.add("김태호")
# print(python)

# # remove
# java.remove("김태호")
# print(java)


# # 자료구조의 변경
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

# # practice4
# from random import *
# user = range(1, 21)  # 1~20 까지 숫자 생성
# user = list(user)
# print(type(user))

# print(user)
# shuffle(user)
# print(user)

# goal = sample(user, 4)

# print("--- 당첨 ---")
# print("치킨 당첨자 : {0}".format(goal[0]))
# print("커피 당첨자 : {0}".format(goal[1:]))


# # 분기
# weather = "비"
# if weather == "비":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")

# weather = input("오늘 날씨는 어때요?")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")

# temp = int(input("기온은 어때요?"))
# if 30 <= temp:
#     print("너무 더워요, 나가지 마세요.")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요, 나가지 마세요.")


# 반복문 for문
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for wait in [0, 1, 2, 3, 4]:
#     print("대기번호 : {0}".format(wait))

# for wait in range(5):  # 0, 1, 2, 3, 4
#     print("대기번호 : {0}".format(wait))

# for wait in range(1, 6):  # 1, 2, 3, 4, 5
#     print("대기번호 : {0}".format(wait))

# guest_list = ["사람1", "사람2", "사람3"]
# for customer in guest_list:
#     print("{0}, 커피가 준비되었습니다.".format(customer))


# 반복문 while
# customer = "손님1"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기 처분되었습니다.")

# customer = "토르"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출{1}회".format(customer, index))
#     index += 1
# ctrl + c로 종료 (무한루프)

# customer = "토르"
# person = "Unknown"

# while person != customer:
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")


# # Continue
# absent = [2, 5]  # 결석
# no_book = [7]
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}교무실".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))


# # 한줄 for
# students = [1, 2, 3, 4, 5]
# print(students)
# students = [i + 100 for i in students]
# print(students)

# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

# # practice 5
# from random import *
# count = 0
# for i in range(1, 51):
#     time = randrange(5, 51)  # 5~50분 사이의 랜덤
#     if 5 <= time <= 15:
#         print("[0] {0}번쨰 손님 (소요시간 : {1}분".format(i, time))
#         count += 1
#     else:  # 매칭 실패한 경우
#         print("[] {0}번쨰 손님 (소요시간 : {1}분".format(i, time))
# print("총 탑승 승객 : {0}".format(count))


# 함수 Def

# def open_account():
#     print("새로운 계좌가 생성되었습니다.")


# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
#     return balance + money


# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
#         return balance


# def withdraw_night(balance, money):
#     commission = 100  # 수수료
#     return commission, balance - money - commission


# balance = 0
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 2000)
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))
# print(balance)


# 기본값
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"
#           .format(name, age, main_lang))


# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"
#           .format(name, age, main_lang))


# profile("유재석")
# profile("김태호")


# 키워드 값
# def profile(name, age, main_lang):
#     print(name, age, main_lang)


# profile(name="유재석", main_lang="파이썬", age="20")
# profile(main_lang="자바", age="25", name="김태호")


# 가변 인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이: {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)


# def profile(name, age, *language):
#     print("이름 : {0}\t나이: {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()


# profile("유재석", 20, "파이썬", "자바", "c", "c++", "c#", "자바스크립트")
# profile("김태호", 25, "코틀린", "스위프트", "", "", "")


# # 지역변수 전역변수
# gun = 10


# def checkpoint(soldiers):
#     global gun  # 전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))


# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun


# print("전체 총 : {0}".format(gun))
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))

# practice 6


# def std_weight(height, gender):
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21


# height = 175
# gender = "남자"
# weight = round(std_weight(height / 100, gender), 2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))


# #  표준 입출력
# import sys
# print("파이썬", "자바", sep=",")
# print("파이썬", "자바", sep=" vs ")
# print("파이썬", "자바", "자바스크립트", sep=" vs ")
# print("파이썬", "자바", sep=",", end="?")
# print("무엇이 더 재미있을까요?")

# print("파이썬", "자바", file=sys.stdout)
# print("파이썬", "자바", file=sys.stderr)

# scores = {"수학": 0, "영어": 50, "코딩": 100}
# for subject, score in scores.items():
#     print(subject, score)

# scores = {"수학": 0, "영어": 50, "코딩": 100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번표
# 001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))

# answer = input("아무 값 입력 : ")
# print("입력하신 값은" + answer + "입니다.")

# # 출력 포맷
# # 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일 땐 +로 표시, 음수일 떈 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<+10}".format(500))
# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(10000000000))
# # 3자리 마다 콤마를 찍어주기, +- 부호도 표시하기
# print("{0:+,}".format(-10000000000))
# print("{0:+,}".format(10000000000))
# # 3자리 마다 콤마를 찍어주기, +- 부호도 표시하기, 자릿수 확보하기
# # 돈이 많으면 행복하니까 빈 자리는 ^로 채워주기
# print("{0:^<+30,}".format(10000000000))
# # 소수점 출력
# print("{0:f}".format(5/3))
# # 소수점 특정 자리수 까지만 표시 (소수점 3쨰 자리에서 반올림)
# print("{0:.2f}".format(5/3))


# # 파일 입출력
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="")  # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")  # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")  # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")  # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()  # list 형태로 저장
# for line in lines:
#     print(line, end="")

# score_file.close()


# pickle
import pickle
# profile_file = open("profile.pickle", "wb")  # 항상 바이너리 저장
# profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

profile_file = open("profile.pickle", "rb")  # 항상 바이너리 저장
profile = pickle.load(profile_file)  # file에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()
