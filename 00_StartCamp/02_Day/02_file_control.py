import os
#os 파일 불러오기

os.chdir(r'C:\Users\student\TIL\00_StartCamp\02_Day\dummy')
#r은 raw라는 뜻인데 ''안의 \를 그대로 봐다란말 dummy들이 있는 파일 넣어라...

for filename in os.listdir('.'):
    os.rename(filename, filename.replace('SAMSUNG_','SSAFY_'))
#     os.rename(filename, f'SAMSUNG_{filename}')
# #현재 디렉토리에 있는 모든 파일들을 가지고 올 것입니다..
# #앞의 리턴값이 리스트기때문에 가능한것


