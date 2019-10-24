from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm,CommentForm

def index(request):
    return render(request, 'articles/index.html')

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form':form,
    }
    return render(request,'articles/create.html',context)

def detail(request, article_pk):
    
    return render(request,'articles/detail.html',article_pk)
# Create your views here.
