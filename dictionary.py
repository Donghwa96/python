# =========================================================
# 필요한 모듈은 이곳에 importing 합니다.
import re
# 필요한 모듈은 이곳에 importing 합니다.
# =========================================================


# =========================================================
# 이곳에 함수를 작성합니다.
def welcome():
    print("hello")
# 인사 기능
def foolsensor():
    input("1더하기 1은? :")
    if int(input())==2 :
        print("당신은 이 사전을 사용할 수 있습니다")
    else:
        print("돌아가십시오")
# 바보 탐지기 기능
def add(a, b):
    k = a + b
    print(k)
# 덧셈 기능
def minus(a, b):
    k = a - b
    print(k)
# 뺄셈 기능
def multi(a, b):
    k = a * b
    print(k)
# 곱셈 기능
def div(a, b):
    k = a / b
    print(k)
# 나눗셈 기능
def remain(a, b):
    k = a % b
    print(k)
# a 를 b로 나누었을 때 남은 나머지를 나타내주는 기능
def rethrow(a, b):
    k = a // b
    print(k)
# a 를 b로 나누었을 때 소수점 아랫자리를 버리는 기능
def square(a, b):
    k =  a ** b
    print(k)
# a의 b승의 값을 나타내는 기능
def slice(a, b):
    k = a[:b]
    print(k)
# a라는 자료형에서 b번호를 가진 값 전까지 나타내주는 기능
def change(a , b):
    k = a(b)
    print(k)
# b라는 자료형을 a자료형으로 바꾸는 기능
# a는 꼭 str,int,dict,tuple,set,list 이 값이여야 함
def same(a , b):
    k = a.count(b)
    print(k)
# 자료형 a에서 b라는 값이랑 같은 값이 자료형 a에 얼마나 있는지 알려주는 기능
# 자료형 a가 str형식이면 b는 ''를 포함하고 작성해야함
def tuple(*x) :
    print(x)
# x에 'one', 'two'이런식으로 넣으면 튜플 형식으로 나오는 기능
def age(x) :
    print('당신의 나이는 input(x)살입니다')
    # 나이를 알려주는 기능
def young(x) :
    if x > 27 :
        print("안타깝다")
    elif x>23 :
        print("보통이다")
    else :
        print("축하한다, 당신은 젊다")
# 자신이 젊은지 알려주는 기능
def bmi(x , y):
    k= y / x**2
    if k > 30 :
        print("고도비만입니다")
    elif k > 24:
        print("경도비만입니다")
    elif k > 20:
        print("정상입니다")
    else :
        print("저체중입니다")
# x에는 자신의 키, y에는 자신의 몸무게 값을 넣으면 자동으로 bmi지수가 측정이 되어서 자신의 몸상태를 알 수 있는 기능
def bodyratio(x, y):
    k = x / y
    if k > 7 :
        print("매우 좋은 비율입니다")
    else :
        print("정상입니다")
# x에는 자신의 키 y에는 자신의 머리 길이 값을 넣으면 자신의 신체비율을 알 수 있는 기능
def impact(a):
    k= a.upper()
    print(k)
# a라는 문자열 자료형에서 소문자를 대문자로 변형시켜주는 기능
def pyramid():
    height = input("피라미드의 높이 : ")
    hei = int(height)
    for k in range(1, hei):
        print("{}".format((hei - k) * " "), "{}".format((2 * k - 1) * "*"), "{}".format((hei - k) * " "))
# 피라미드를 만들고 싶을때 만들어주는 기능, 몇층이든 상관이 없다! 다 가능
def foodrecommend():
    a= input("뭐 먹고 싶어? : ")
    if a == "음식" :
        print("돼지갈비, 피자, 삼겹살, 김치찌개, 황금올리브치킨을 추천해~")
    elif a == "음료" :
        print("버블티, 카페모카, 아포가토, 청포도에이드, 깔라만시에이드를 추천해~")
    elif a == "디저트" :
        print("치즈케이크, 크로크무슈, 커피번, 티라미슈를 추천해~")
    else:
        print("그런거 말고 음식, 음료, 디저트를 입력해봐~")
# 배고플때 결정 장애가 오는 친구들에게 컴퓨터가 추천해주는 기능
def dorecommend():
    do = input("뭐 하고 싶어? : ")
    if do == '휴식' :
        print('공부는 다 했어?')
    elif do == '공부':
        print("공부 열심히 하네~")
    else :
        print("맘대로 해~")
# 지금 뭘 해야 될지 아무 생각이 안 날 때 직접 추천해주는 기능
def canIcoffee():
        money = int(input("당신은 현재 돈이 얼마나 있습니까:"))
        if money >3000 :
            print("커피 한잔 할 수 있겠네요")
        elif money > 2000 :
            print("그럼 아이스티라도 괜찮으시다면...")
        else :
            print("요즘은 자판기 커피도 맛있습니다")
# 자신이 커피 한잔의 여유는 가지고 있는가를 알 수 있는 기능
def even():
    k = input("수를 입력하세요: ")
    n= int(k)
    if n % 2 ==0:
        print('{0}는 짝수입니다'.format(n))
    else :
        print("홀수 입니다")
# 짝,홀수 탐지기 기능
def listsum():
    a = int(input("1번값: "))
    b = int(input("2번값: "))
    c = int(input("3번값: "))
    d = int(input("4번값: "))
    e = int(input("5번값: "))
    f= int(input("얼마 이상을 원하오? :"))
    A= [a, b, c, d, e]
    result = 0
    while A:
        mark = A.pop()
        if mark >= f:
            result += mark
    print(result)
# a라는 리스트 에서 b값보다 더 높은 값들의 합을 구하는 기능
def fail():
    a = int(input("1번 학생의 점수를 입력하세요: "))
    b = int(input("2번 학생의 점수를 입력하세요: "))
    c = int(input("3번 학생의 점수를 입력하세요: "))
    d = int(input("4번 학생의 점수를 입력하세요: "))
    e = int(input("5번 학생의 점수를 입력하세요: "))
    f = int(input("합격컷을 입력하세요: "))
    marks = [a, b, c, d, e]
    number = 0
    for mark in marks:
        number = number + 1
        if mark >= f:
            print("%d 응시자는 합격입니다"%number)
        else:
            print("%d 응시자는 불합격입니다"%number)
# 합,불합 판정 기능
def gogo():
    a = int(input("구구단 몇단을 원하십니까? "))
    for i in range(a,10):
        for j in range(1,10):
            print(i*j)
        print('')
# 구구단 기능
def scoregrader(mid, final) :
    total = (mid + final)/2
    if total >= 90 :
        print('A학점')
    elif total >= 80 :
        print('B학점')
    elif total >= 70 :
        print('C학점')
    elif total >= 60 :
        print('D학점')
    else :
        print('당신은 학사경고를 받았습니다')
# 학점계산기 기능
def fahrenheit():
    fahren = int(input("현재 화씨를 적어주세요: "))
    celcius = (fahren-32)/ 1.8
    print(celcius)
# 화씨계산기 기능
def trianglearea(bottom,height):
    area = bottom*height/2
    print(area)
# 삼각형 넓이 구하기 기능
def partpay():
    hour = int(input("일한 시간을 입력하세요: "))
    timepay = int(input("시급을 입력하세요: "))
    if hour < 40 :
        pay = hour * timepay
        print(pay)
    else:
        pay = ((hour-40)* 1.5 * timepay) + 40* timepay
        print(pay)
# 시급계산기 (40시간하면 초과수당시급 1.5배)
# 이곳에 함수를 작성합니다.
# =========================================================


# =========================================================
# 따로 설정할 필요 없습니다.

def main():
    print("함수 사전 목록을 불러옵니다.")


if __name__ == "__main__":
    main()
    func_list = []

    for i in dir():
        if re.search('[__]+', i) or i == "i" or i == "re" or i == "main":
            pass
        else:
            func_list.append(i)

    for num, func in enumerate(func_list, start=1):
        print("{0}: {1}".format(num, func))

# 따로 설정할 필요 없습니다.
# =========================================================
dorecommend()
partpay()
listsum()
fail()
fahrenheit()
scoregrader(80,95)
welcome()
add(1,2)
minus(2,1)
multi(5,4)
div(18,4)
remain(28,6)
rethrow(154,17)
square(15,9)
a = "hello"
slice(a,4)
b= "4"
change(int,b)
c= "Hello my name is park dong hwa"
d="e"
same(c,d)
tuple(*d)
young(24)
bmi(190,76)
bodyratio(190,27)
impact(a)
pyramid()
foodrecommend()
canIcoffee()
even()
fail()
gogo()


