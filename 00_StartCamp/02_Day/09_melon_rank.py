import requests
from bs4 import BeautifulSoup

#딕셔너리에 멜론 페이지 > 검사 > 네트워크 > ctrl+r > name Headers > requests > 요청하는 사람이 헤더 정보를 넘겨줘야하는거>useragent 다 긁기
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
response = requests.get("https://www.melon.com/chart/index.htm", headers=headers)
response.encoding = 'utf-8'
res = response.text

soup = BeautifulSoup(res, 'html.parser')

songs = soup.select('.lst50') #.는 클래스란 뜻, select는 list로 반환

for song in songs:
    rank = song.select_one('#lst50 > td:nth-child(2) > div > span.rank').text
    name = song.select_one('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    artist = song.select_one('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
    print(f'{rank}위 : {name} / {artist}')

#csv 파일로 옮기기
with open('melon.csv','w', encoding='utf-8') as f:
    for song in songs:
        rank = song.select_one('#lst50 > td:nth-child(2) > div > span.rank').text
        name = song.select_one('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
        artist = song.select_one('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
        f.write(f'{rank}위 : {name} / {artist}\n')
