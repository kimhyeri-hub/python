#6장 예제_

import turtle as t

#색상 리스트에 저장
colors=["red","purple","blue","green","yellow","orange"]

#배경색 변경
t.bgcolor("black")

#거북이의 속도 0으로 설정(최대 속도)
t.speed(0)

#거북이의 선 두께 설정
t.width(3)
#초기 선의 길이는 10
length=10

while length < 500:
    t.forward(length)
    t.pencolor(colors[length%6])
    t.right(89)
    length+=5

t.done()
