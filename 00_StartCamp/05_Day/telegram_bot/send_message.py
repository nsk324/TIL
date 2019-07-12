#파이썬 코드로 텔레그램 메시지 보내기
from decouple import config 
import requests

api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
text = '오늘 너에게 나의 삼계탕을 양보할게'

send_message = requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

print(send_message.text)

#이렇게 변수화 하는 이유는 여러군대에서 변수를 사용할 수 있기 때문입니다.