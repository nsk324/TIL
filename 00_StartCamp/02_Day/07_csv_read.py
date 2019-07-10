# # csv 파일 read의 두 가지 방법

# #1. split 
# with open('lunch.csv','r',encoding='utf-8') as f:
#     lines = f.readlines() # 리스트 타입
#     for line in lines:
#         print(line.strip()) # 개행되는부분들이 사라지도록
#         print(line.strip().split(','))#, 를 기준으로 list 형식으로 반환
#         print(type(line))


#2. scv reader

import csv ## csv조작할때 쓰는거

with open('lunch.csv', 'r', encoding='utf-8') as f:
    lines = csv.reader(f)

    for line in lines:
        print(line) #line 이라는 list 형태의 자료형이다.