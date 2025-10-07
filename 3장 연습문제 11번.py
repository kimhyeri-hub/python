# 4주차_3장 연습문제 11번

#시간 모듈 불러오기 
import time

# 1970년 이후 흘러온 초가 실수로 반환
fseconds = time.time()
total_sec = int(fseconds)

# 흘러온 초를 분으로 바꾸고, 현재 몇 분인지 계산
total_min = total_sec // 60
minute = total_min % 60

# 흘러온 분을 시간으로 바꾸고, 현재 몇 시인지 계산
total_hour = total_min // 60 
hour = total_hour % 24        

print("현재 시간(영국 그리니치 시각): " + str(hour) + "시 " + str(minute) + "분")
