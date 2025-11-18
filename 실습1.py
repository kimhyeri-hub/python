#사용자에게 2이상의 정수 n과 연산자를 입력받아 연산자가 곱하기이면 1~n까지 곱을 계산
'''
n = int(input("정수를 입력하세요: "))
op = input("연산자를 선택하세요 (+ 또는 *): ")

if op == '+':
    result = sum(range(1, n + 1))
elif op == '*':
    result = 1
    for i in range(1, n + 1):
        result *= i

print("결과:", result)
'''

#함수 사용하기


n = int(input("정수를 입력하세요: "))
op = input("연산자를 선택하세요 (+ 또는 *): ")

def cal(n,op):
    if op == '+':
        result = sum(range(1, n + 1))
    elif op == '*':
        result = 1
        for i in range(1, n + 1):
            result *= i

    return result

result=cal(n,op)
print("결과: ", result)
