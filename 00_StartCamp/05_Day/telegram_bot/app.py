from flask import Flask, render_template, request
from decouple import config 
import requests

app = Flask(__name__)

api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')

naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    text = request.args.get('message')
    requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    
    return render_template('send.html')

@app.route(f'/{token}', methods=['POST']) #아무나 들어오지못하도록 token 그리고 플라스크가 post 요청을 보냅니다.
def telegram():
    #1. 구조 print 해보기 & 변수 저장
    from_telegram = request.get_json()
    print(from_telegram)

    #2. 메시지를 그대로 돌려 보내기
    if from_telegram.get('message') is not None :
        chat_id = from_telegram.get('message').get('from').get('id')
        # print(chat_id)
        text = from_telegram.get('message').get('text')
      
        
        #3. keyword(번역)
        if text[0:4] == '/번역 ':
            headers = {'X-Naver-Client-ID': naver_client_id, 'X-Naver-Client-Secret': naver_client_secret} # 네이버가 요구한 방식
            data = {'source': 'ko', 'target': 'en', 'text': text[4:]}
            
    
            papago_res =requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data) #post 요청방식을 사용
            print(papago_res)
            text = papago_res.json().get('message').get("result").get("translatedText")
            print(text)
        res = requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    return '', 200 




