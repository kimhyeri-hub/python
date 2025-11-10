# 팩토리얼 계산_ 정수값을 입력받아 팩토리얼 계산하고 출력

n = int(input("정수를 입력하시오: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print(f"{n}!은 {fact}입니다.")


#2 정수값을 입려갇아 "팩토리얼 값을 계산하는 함수로 작성"하고 호출하기

n = int(input("정수를 입력하시오: "))

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(f"{n}!은 {factorial(n)}이다.")

#3 정수값을 입력받아 팩토리얼값을 계산하는 함수 작성하고 호출하기를 반복
# 사용자가 0을 입력하면 프로그램 종료


def factorial(n):   
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

while True:     #팩토리얼 반복
    n = int(input("정수를 입력하시오 (0 입력하면 종료): "))
    if n == 0:
        print("프로그램을 종료합니다.")
        break
    print(f"{n}!은 {factorial(n)}입니다.")

#4 팩토리얼 함수를 재귀함수로 정의하기

def factorial(n):
    
    if n==1:
        return 1
    return factorial(n-1)*n

