#  편의점 재고 관리 프로그램_ 재고를 딕셔너리에 저장하기
'''
items_dic={"커피": 7,"펜": 3, "종이컵": 2,"우유": 1, "콜라":4,"책":5}

item=input("물건의 이름을 입력하시오:")
print(items_dic[item])
'''

# 신규물품 재고 등록하는 함수 추가하기
def insert_item():
    item_name=input("물품명 입력: ")
    item_dic[item_name]=int(input("물품의 재고량: "))
    print("등록완료")

#재고증량
def inc_cnt():
    item_name=input("물품명 입력: ")
    item_dic[item_name]+=int(input("증가량: "))
    print("등록완료")

#재고량 감소
def dec_cnt():
    item_name=input("물품명 입력: ")
    item_dic[item_name]-=int(input("감소량: "))
    print("등록완료")

#물품삭제
def delete_item():
    item_name=input("물품명 입력: ")
    item_dic.pop(item_name)
    print("삭제 완료")
    
#전체 물품 출력    
def all_item_print():
    for item_name in sorted(item_dic.keys()):
        print(item_name, item_dic[item_name])



#전역변수 생성
msg="1.물품등록 2.재고증량 3.재고량 감소 4.물품삭제 5.전체물품 출력 6. 종료: "

item_dic={}
#소스가 긴 경우 여기서부터 실행문장 시작이라고 소스를 읽는 다른 프로그래머에게 알리는 관용구
if __name__=='__main__':
    while True:
        n=int(input(msg))

        if n==1:
            insert_item()
        elif n==2:
            inc_cnt()
        elif n==3:
            dec_cnt()
        elif n==4:
            delete_item()
        elif n==5:
            all_item_print()
        elif n==6:
            print("프로그램 종료")
            break
        else:
            print("1~6중에서 선택하세요")
            
