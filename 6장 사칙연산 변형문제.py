#무작위로 2자리 숫자 사칙연산을 출력해서 결과값을 물어보는 산수퀴즈 + 사용자에게 계속할 지를 물어본 후 'yes'라고 답하면 산수퀴즈를 계속한다.

import random

# 초기값 설정
input_user = 'yes'

# 퀴즈 반복
while input_user == 'yes':
    # 2개의 2자리 숫자 무작위로 생성
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)

    # 연산자 무작위 선택
    operators = ['+', '-', '*', '/']
    op = random.choice(operators)

    # 문제 출력
    print(f"\n문제: {num1} {op} {num2} = ?")
    input("정답을 입력하세요: ")  

    # 계속할지 묻기
    input_user = input("계속 하려면 'yes'를 입력하세요: ")

print("퀴즈를 종료합니다. ")
