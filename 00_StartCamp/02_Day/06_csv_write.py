lunch = {
    '양자강': '054',
    '김밥카페': '051',
    '순남시래기': '053'
}
#딕셔너리

#1. 방법 1
#.items() 튜플 형태로 나옴 ('양자강, '054') (0,1)
# 한글 깨짐을 막기 위해 인코딩 인자 넣어주기
with open('lunch.csv', 'w', encoding='utf-8') as f:
    for item in lunch.items():       
        f.write(f'{item[0]},{item[1]}\n')



