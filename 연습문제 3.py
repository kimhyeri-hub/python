# 연습문제3번, 3개 숫자를 사용자로부터 입력받아 합과 평균값 출력하기 
num1 = int(input("숫자1를 입력하세요: "))
num2 = int(input("숫자2를 입력하세요: "))
num3 = int(input("숫자3를 입력하세요: "))

sum = num1 + num2 + num3
avg = sum / 3

print("숫자1:", num1)
print("숫자2:", num2)
print("숫자3:", num3)
print("숫자의 합은:", sum)
print("숫자의 평균은:", avg)
