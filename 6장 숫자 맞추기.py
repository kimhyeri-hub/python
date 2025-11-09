#6장 실습_숫자 맞추기 게임 1부터 100까지의 난수를 사용자가 맞추며 시도 횟수를 출력하는 프로그램 

import random

tries = 0
guess = 0
answer = random.randint(1,101)

print("1부터 100 사이의 숫자를 맞추세요")

while guess != answer and tries<10:
    guess=int(input("숫자를 입력하세요: "))
    tries +=1
    
    if guess<answer:
        print("낮음")
    if guess>answer:
        print("높음")
        
if guess==answer:
    print("정답입니다. 시도횟수=",tries)
else:
    print("정답은", answer)
