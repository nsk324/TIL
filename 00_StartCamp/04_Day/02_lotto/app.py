from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests
#각 위치마다 가져올수있는 함수가 다름

app = Flask(__name__)

@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')   
#그저 html만(첫화면) 보여줌

@app.route('/lotto_result')
def lotto_result():
    num = request.args.get('num') #폼으로 날린 데이터를 받을때
    res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}') #받은 번호를 넣어야 하기 때문에 f스트링을 사용하여 동적으로 바꿔줍니다.
    lotto = res.json() #json 자료형식이 lotto에 담김. dictionary임)

    #1. 번호 6개 가져오기
    winner = []
    for i in range(1, 7):
        winner.append(lotto[f'drwtNo{i}']) #위너에 append(추가합니다.) lotto라는 딕셔너리에서 가져옵니다.

    #2. 내 번호 리스트 만들기
    numbers = []
    for num in request.args.get('numbers').split(): #list로 만들어 줍니다.
        numbers.append(int(num))

    if len(numbers) == 6:
        #번호 교집합 개수 찾기
        matched = 0
        for num in numbers:
            if num in winner:
                matched += 1
        
        if matched == 6:
            result = '1등입니다!!!(퇴사)'
        elif matched == 5:
            if lotto['bnusNo'] in numbers:
                result = '2등입니다!!!(탈조선)'
            else:
                result = '3등입니다!!!(소고기)'
        elif matched == 4:
            result = '4등입니다!!!(택시)'
        elif matched == 3:
            result = '5등입니다!!!(복권)'
        else:
            result = '꽝입니다!!!(돈날림)'

    else:
        result = '번호의 수가 6개가 아닙니다.'
    return render_template('lotto_result.html', winner=winner, numbers=numbers, result=result)