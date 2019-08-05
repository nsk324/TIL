from django.shortcuts import render
from datetime import datetime
import random

# Create your views here.
# 1.기본로직
def index(request):
    return render(request, 'index.html')

def introduce(request):
    return render(request, 'introduce.html')

def image(request):
    return render(request, 'image.html')

#2. Template Variable (템플릿 변수)
def dinner(request):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)# optional
    context = {'pick': pick}
    return render(request, 'dinner.html', context) #3번째 자료형은 반드시 dictionary

#3. Variable Routing (동적 라우팅)
def hello(request, name, age):
    menu = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menu)
    context = {
        'name': name,
        'age': age,
        'pick':pick
    }
    return render(request, 'hello.html', context)

#4. 실습
#4-1. 동적 라우팅을 활용해서 (name과 age를 인자로 받아) 자기 소개 페이지
def hi(request, name, age):
    context = {
        'name': name,
        'age' : age
    }
    return render(request, 'hi.html', context)
#4-2. 두 개의 숫자를 인자로 받아(num1, num2) 곱셈 결과를 출력
def multi(request, num1, num2):
    context = {
        'num1': num1,
        'num2': num2,
        'answer' : num1*num2
    }
    return render(request, 'multi.html', context)

#4-3. 반지름(r)을 인자로 받아 원의 넓이(area)를 구하시오
def area(request, r):
    context = {
        'r' : r,
        'area' : r**2 * 3.14
    }
    return render(request, 'area.html', context)

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
        'datetimenow': datetimenow
    }
    return render(request, 'template_language.html', context)


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
    return render(request, 'student.html', context)