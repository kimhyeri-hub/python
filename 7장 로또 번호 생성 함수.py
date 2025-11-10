# 7장_ 로또 번호 생성 함수 (변형)
#사용자에게 몇 개의 로또번호를 생성할지 물어보고 해당 개수만큼 로또번호 생성해서 출력하기

import random

def getLotto():
    numbers = []
    while len(numbers) < 6 :
        n = random.randint(1,45)
        if n not in numbers:
            numbers.append(n)
    return numbers

s=int(input("로또 생성 횟수"))

for i in range(s):
    print(f"생성된 로또 번호{getLotto()}")

