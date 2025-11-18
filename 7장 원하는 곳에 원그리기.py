#클릭하는 곳에 원 그리기
#크기와 색깔 랜
import turtle as t
import random as r

def myCircle(length):
    t.circle(length)
    
def drawit(x,y):
    length=r.randint(1,99) 
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.color(r.random(),r.random(),r.random()) #랜덤 색상 지정
    myCircle(length)
    t.end_fill()

s=t.Screen()    #그림이 그려지는 화면을 얻는다.
s.onscreenclick(drawit) #마우스 클릭 이벤트 처리 함수를 등록.

t.done()
