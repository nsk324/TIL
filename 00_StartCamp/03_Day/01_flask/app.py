from flask import Flask
import datetime
import random
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world!'

@app.route('/ssafy')
def ssafy():
    return '왕 크다 왕 맛있다'

@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    endgame = datetime.datetime(2019, 11, 29)
    td = endgame - today
    return f'사피 1학기 종료까지 {td.days}일 남았습니다.'#일수로 나옴

@app.route('/html')
def html():
    return '<h1>This is HTML h1 tag!<h1>' #테그 열면 테그 닫아줘야함

@app.route('/html_line')#/하면 클로징 의미
def html_line():
    return """
    <h1> 여러줄로 작성하자~!~!~! 우끼끼 </h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    """

@app.route('/greeting/<string:name>') ##뭔가 특별하게 생김...
def greeting(name):
    return f'반갑습니다. {name}님~!'

@app.route('/cube/<int:number>') ##세제곱을 하는걸 받을거임
def mul(number):
    return f'{number}의 세 제곱은 {number**3}입니다.'

#점심 메뉴 리스트(다섯 개)에서 n명의 사람개 뽑아 출력 하기
@app.route('/lunch/<int:person>')
def lun(person):
    menu = ["아몬드치킨샌드위치", "쇠고기볶음", "갈치카레구이", "빨간우동", "프라이두부샐러드"]
    order = random.sample(menu, person)
    return str(order)