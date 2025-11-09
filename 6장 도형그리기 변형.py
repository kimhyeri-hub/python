#6장 실습 그림판_선택_반복_다각형 그리기

#5장_예제 도형그리기
#사용자에게 n각형 그릴 건지 입력받아 다각형 그리기

import turtle as t
t.shape("turtle")

#교수님 버전
t.up()
t.goto(0,0)
t.down()
n=int(t.textinput("","3,4,5,6 어떤 다각형을 그릴까요: "))

if n==3 or n==4 or n==5 or n==6:

    angle=360/n

    t.up()
    t.goto(0,-200)
    t.down()
    for i in range(n):
        t.fd(100)
        t.right(angle)
else:
    t.write("잘못 입력")

'''
#사용자에게 몇 각형을 받을 건지 메세지 출력
n=int(t.textinput("","3,4,5,6 어떤 다각형을 그릴까요: "))


t.penup()
t.goto(0,0)
t.pendown()
if n==3 : #삼각형 그리기
    for i in range(3):
        t.forward(100)
        t.left(120)
    
elif n==4 : #사각형 그리기
     for i in range(4):
        t.forward(100)
        t.left(90)
    
elif n==5 : #오각형 그리기
    for i in range(5):
        t.forward(100)
        t.left(72)
    
elif n==6 :#육각형 그리기
     for i in range(6):
        t.forward(100)
        t.left(60)

else : #그 외의 숫자를 입력했을 때 
    t.write("잘못된 입력입니다.")

'''

