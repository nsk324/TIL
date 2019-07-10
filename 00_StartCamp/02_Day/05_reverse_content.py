# 파일에 잇는걸 다 가져온다 (list)/ 꺼굴로 돌린다 / 다시 파일 만든다

#1. 각각의 라인을 리스트의 요소로 불러오기
with open('writelines_ssafy.txt', 'r') as f:
    lines = f.readlines()

#2. 뒤집기
lines.reverse() #원본 뒤집기

#3. line 을 작성하기 ( 뒤집 은걸 하나씩 꺼내서 써주면 된다)

with open('reverse_ssafy.txt', 'w') as f:
    for line in lines:
        f.write(line)
