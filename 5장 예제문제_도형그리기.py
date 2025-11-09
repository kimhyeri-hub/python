#5장_예제 도형그리기
#사용자에게 n각형 그릴 건지 입력받아 다각형 그리기

import turtle as t
t.shape("turtle")

#사용자에게 몇 각형을 받을 건지 메세지 출력
n=int(t.textinput("","3,4,5,6 어떤 다각형을 그릴까요: "))


t.penup()
t.goto(0,0)
t.pendown()
if n==3 : #삼각형 그리기
    t.forward(100)
    t.left(90)
    t.left(30)
    t.forward(100)
    t.left(120)
    t.forward(100)
    
elif n==4 : #사각형 그리기
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    
elif n==5 : #오각형 그리기
    t.forward(100)
    t.left(72)
    t.forward(100)
    t.left(72)
    t.forward(100)
    t.left(72)
    t.forward(100)
    t.left(72)
    t.forward(100)
    t.left(72)
    
elif n==6 :#육각형 그리기
    t.forward(100)
    t.left(60)
    t.forward(100)
    t.left(60)
    t.forward(100)
    t.left(60)
    t.forward(100)
    t.left(60)
    t.forward(100)
    t.left(60)
    t.forward(100)
else : #그 외의 숫자를 입력했을 때 
    t.write("잘못된 입력입니다.")
