#사용자에게 자동차 크기, 색깔 입력 받아 자동차 그리기
import turtle
t = turtle.Turtle()
t.shape("turtle")

# 사용자로부터 자동차의 크기를 받아서 size라는 변수에 저장

size = int(input("자동차의 크기는 얼마로 할까요?"))
size2 = int(input("자동차 바퀴의 크기는 얼마로 할까요?"))

# 사용자로부터 자동차의 색깔을 받아서 color라는 변수에 저장

color1 = input("자동차의 몸통색깔은 무엇으로 할까요?")
color2 = input("자동차의 하단색깔은 무엇으로 할까요?")

#자동차 몸체
t.up()
t.goto(-2*size,-0.5*size)
t.down()
t.fillcolor(color1)
t.begin_fill()
t.forward(4*size)
t.left(90)
t.forward(2*size)
t.left(90)
t.forward(4*size)
t.left(90)
t.forward(2*size)
t.end_fill()

#자동차 상단 
t.up()
t.goto(-size, 2.5*size)
t.down()
t.fillcolor(color2)
t.begin_fill()
t.forward(size)
t.left(90)
t.forward(2*size)
t.left(90)
t.forward(size)
t.left(90)
t.forward(2*size)
t.end_fill()

#자동차 왼쪽 바퀴 
t.up()
t.goto(-1.3*size, -0.05*size)
t.down()
t.color("black")
t.begin_fill()
t.circle(size2)
t.end_fill()
#자동차 오른쪽 바퀴
t.up()
t.goto(1.3*size, -0.05*size)
t.down()
t.color("black")
t.begin_fill()
t.circle(size2)
t.end_fill()

