from django.shortcuts import render
# Create your views here.

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