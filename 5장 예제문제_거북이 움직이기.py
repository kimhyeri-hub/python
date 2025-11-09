#예제_ 사용자로부터 정수를 받아서 정수의 부호에 따라 거북이를 움직이는 프로그램
#(100,100),(100,0),(100,-100)

#그림 모듈
import turtle as t
t.shape("turtle")

#사용자에게 입력을 받는 메세지(그림판에서 입력)
s=t.textinput("","숫자를 입력하세요: ")

n=int(s)

t.penup()
t.goto(100,100)
#화면에 메시지 출력
t.write("여기는 양수입니다.")
t.goto(100,0)
t.write("여기는 0입니다.")
t.goto(100,-100)
t.write("여기는 음수입니다.")

t.goto(0,0)
t.pendown()

if n>0 :
    t.goto(100,100)
elif n==0 :
    t.goto(100,0)
else :
    t.goto(100,-100)

t.done()
