#6장 실습_ 구구단 출력

print("구구단 출력\n")

# 단 이름 출력
for dan in range(2, 10):
    print("==%d단==" % dan, end=" | ")
print()  # 줄 바꿈

# 구구단 내용 출력
for i in range(1, 10):
    for dan in range(2, 10):
        print("%d*%2d=%2d" % (dan, i, dan * i), end=" | ")
    print()
