from django.shortcuts import render
from datetime import datetime
import random
import requests

# Create your views here.
# 1.기본로직
def index(request):
    return render(request, 'pages/index.html')

def introduce(request):
    return render(request, 'pages/introduce.html')

def image(request):
    return render(request, 'pages/image.html')

#2. Template Variable (템플릿 변수)
def dinner(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)# optional
    context = {'pick': pick}
    return render(request, 'pages/dinner.html', context) #3번째 자료형은 반드시 dictionary

#3. Variable Routing (동적 라우팅)
def hello(request, name, age):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {
        'name': name,
        'age': age,
        'pick':pick
    }
    return render(request, 'pages/hello.html', context)

#4. 실습
#4-1. 동적 라우팅을 활용해서 (name과 age를 인자로 받아) 자기 소개 페이지
def hi(request, name, age):
    context = {
        'name': name,
        'age' : age
    }
    return render(request, 'pages/hi.html', context)
#4-2. 두 개의 숫자를 인자로 받아(num1, num2) 곱셈 결과를 출력
def multi(request, num1, num2):
    context = {
        'num1': num1,
        'num2': num2,
        'answer' : num1*num2
    }
    return render(request, 'pages/multi.html', context)

#4-3. 반지름(r)을 인자로 받아 원의 넓이(area)를 구하시오
def area(request, r):
    context = {
        'r' : r,
        'area' : r**2 * 3.14
    }
    return render(request, 'pages/area.html', context)

#5. DTL(Django Template Language)

def template_language(request):
    menus = ['짜장면','짬뽕','탕수육','멘보샤']
    my_sentence = "Life is short, you need python"
    message = ['apple', 'banana', 'cucumber', 'mango']
    empty_list = []
    datetimenow = datetime.now


    context = {
        'menus':menus,
        'my_sentence': my_sentence,
        'messages': message,
        'empty_list':empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'pages/template_language.html', context)


def info(request):
    return render(request, 'info.html')

def student(request, name):

    people = {
        '김밥' : 13,
        '천국' : 14,
    }

    context = {
        'name' : name,
        'age' : people.get(name)
    }
    return render(request, 'pages/student.html', context)

    #6. 실습
    #6-1. isbirth

def isbirth(request):
    today = datetime.now()
    if int(today.month) == 3 and int(today.day) ==24:
        result = True
    else:
        result = False
    context = {
        'result': result,
    }
    return render(request, 'pages/isbirth.html', context)

    #6-2. 회문판별(palindrome)
def ispal(request, word):
    if word == word[::-1]:
        result = True
    else:
        result = False

    context = {
        'word' : word,
        'result' : result,
    }
    return render(request, 'pages/ispal.html', context)

#6-3. 로또
def lotto(request):
    real_lottos = [21, 24, 30, 32, 40, 42]
    lottos = sorted(list(random.sample(range(1,46),6)))
    context = {
        'lottos': lottos,
        'real_lottos': real_lottos,
    }
    return render(request, 'pages/lotto.html', context)


#7. Form - GET

def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    context = {
        'message':message,
        'message2':message2,
    }
    return render(request, 'pages/catch.html', context)

def ping(request):
    return render(request, 'pages/ping.html')

def pong(request):
    p1 = request.GET.get('p1')
    context = {
        'p1':p1,
    }
    return render(request, 'pages/pong.html', context)


#8. Form-GET 실습(아스키 아티)
def art(request):
    return render(request, 'pages/art.html')

def result(request):
    #1. form으로 날린 데이터를 받는다. (GET)
    word = request.GET.get('word')
    
    #2. ARTII api로 요청을 보내 응답 결과를 fonts에 저장한다.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
    
    #3. fonts(str)를 fonts(list)로 바꾼다.
    fonts = fonts.split('\n')

    #4. fonts(list)안에 들어있는 요소 중 하나를 선택하여
    # font라는 변수에 저장(str)
    font = random.choice(fonts)

    #5. 위앳 사용자에게 받은 word와 font를 가지고 다시 요청을 보냄
    # 응답 결과를 result에 저장한다.(text로)
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text

    context = {
        'result':result,
    }
    return render(request, 'pages/result.html', context)

#9. Form - Post
def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {
        'name':name,
        'password': pwd,
    }
    return render(request, 'pages/user_create.html', context)


#10. 정적 파일
def static_example(request):
    return render(request, 'pages/static_example.html')