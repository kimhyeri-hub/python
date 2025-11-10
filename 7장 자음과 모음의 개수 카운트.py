#7장 자음과 모음의 개수 카운트하기

def countVowelConsonant(string):
    vowel_count = 0         #모음의 개수 초기값 0
    consonant_count = 0     #자음의 개수 초기값 0
    for ch in string:
            if ch in ['a', 'e', 'i', 'o', 'u']:
                vowel_count += 1
            else:   #자음
                consonant_count += 1
    return vowel_count, consonant_count

s = input("문자열을 입력하시오: ")
n, k = countVowelConsonant(s)
print(f"모음의 개수는 {n}개 입니다.")
print(f"자음의 개수는 {k}개 입니다.")
