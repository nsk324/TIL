#1. 딕셔너리 만들기

lunch = {
    '중국집':'02'
}

"""
2. 딕셔너리 내용 추가하기
#함수로 dictionary 만드는 방법 
# 처음 중국집에 ''붙이면안됩니다.
"""

lunch = dict(중국집='02')
#print(lunch)

#dictionary에 저장하고시프세여?
lunch['분식집'] = '031'
# print(lunch)

#딕셔너리의 내용을 가져와보겠읍니다.
"""
3. 딕셔너리 값 가져오기
"""
idol = {
    'bts': {
        '지민':24,
        'RM':25
    }
}

# print(idol['bts']['RM'])
# #key로 value를 가지고 올 수 있음 (1)

# print(idol.get('bts').get('RM'))
# #key로 value를 가지고 올 수 있음 (2)

"""
4. 딕셔너리 반복문 활용하기
"""
#4-1 기본활용

# for key in lunch:
#     print(key)
#     print(lunch[key])

#4-2 .items() - key, value 모두 가져오기
# for key, value in lunch.items():
#     print(key, value)

#4-3 .values() - value만 가져오기
# for value in lunch.values():
#     print(value)

#4-4 .keys() - key만 가져오기
for key in lunch.keys():
    print(key)