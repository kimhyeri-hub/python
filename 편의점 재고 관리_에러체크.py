# <편의점 물품 재고 관리>
'''
에러체크
1. 관리하는 물품 개수는 50개를 넘을 수 없음.
2. 신규물품등록할 때 이미 등록된 물품이면 에러처리
3. 재고량 증감, 물품삭제 작업 전 등록된 물품인지 확인
4. 재고량 감소시 재고량이 음수가 되지 않는지 확인
'''

# 에러 체크 함수
def error1():
    return len(item_dic) >= 50

def error2(item_name):
    return item_name in item_dic

def error3(item_name):
    return item_name not in item_dic

def error4(item_name, amount):
    return item_dic[item_name] - amount < 0

# 신규물품 재고 등록하는 함수
def insert_item():
    item_name = input("물품명 입력: ")
    if error1():
        print("50개를 넘을 수 없습니다.")
        return
    if error2(item_name):
        print("이미 등록된 물품입니다.")
        return

    item_dic[item_name] = int(input("물품의 재고량: "))
    print("등록완료")

# 재고 증량
def inc_cnt():
    item_name = input("물품명 입력: ")
    if error3(item_name):
        print("등록되지 않은 물품입니다.")
        return

    item_dic[item_name] += int(input("증가량: "))
    print("등록완료")

# 재고량 감소
def dec_cnt():
    item_name = input("물품명 입력: ")
    if error3(item_name):
        print("등록되지 않은 물품입니다.")
        return

    amount = int(input("감소량: "))
    if error4(item_name, amount):
        print("감소할 수 없습니다.")
        return

    item_dic[item_name] -= amount
    print("등록완료")

# 물품 삭제
def delete_item():
    item_name = input("물품명 입력: ")
    if error3(item_name):
        print("등록되지 않은 물품입니다.")
        return

    item_dic.pop(item_name)
    print("삭제 완료")

# 전체 물품 출력
def all_item_print():
    for item_name in sorted(item_dic.keys()):
        print(item_name, item_dic[item_name])

# 전역변수 생성
msg = "1.물품등록 2.재고증량 3.재고량 감소 4.물품삭제 5.전체물품 출력 6. 종료: "
item_dic = {}

# 실행부
if __name__ == '__main__':
    while True:
        n = int(input(msg))

        if n == 1:
            insert_item()
        elif n == 2:
            inc_cnt()
        elif n == 3:
            dec_cnt()
        elif n == 4:
            delete_item()
        elif n == 5:
            all_item_print()
        elif n == 6:
            print("프로그램 종료")
            break
        else:
            print("1~6중에서 선택하세요")
