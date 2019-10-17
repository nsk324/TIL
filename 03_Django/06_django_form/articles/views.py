from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from IPython import embed

def index(request):
    articles = Article.objects.all()
    context = {'articles':articles,}
    return render(request, 'articles/index.html',context)

def create(request):
    '''
    Form Class
    - 모델에 대한 정보를 알지 못해서 유효성 검사 이후에 cleaned_data를
     통해 데이터 정제 후 DB에 실제 저장하는 로직 필요

    Model Form
    이미 model에 대한 정보(schema)를 알고 있기 때문에 어떤 모델에 정보를
    넣어야 하는지 알고있기에 form.save()만 해도 DB에 저장됨 
    '''
    if request.method == 'POST':
        # form 인스턴스를 생성하고 요청에 의한 데이터로 채운다.
        form = ArticleForm(request.POST)
        # 해당 폼이 유효한지 확인
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
        context = {'form':form,}
        return render(request, 'articles/form.html',context)

def detail(request, article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    # article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm()
    comments = article.comments.all()
    #comments = article.comment_set.all()
    context = {
        'article':article,
        'comment_form':comment_form,
        'comments':comments,
        }
    return render(request, 'articles/detail.html',context)
@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index') # redirect -> GET 요청
   
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method=='POST':
        # instance -> 수정의 대상이 되는 특정한 글 객체
        form = ArticleForm(request.POST, instance=article) # 인스턴스 생성
        if form.is_valid():
            form.save()
            #embed() 글 업뎃이 안됨
            return redirect('articles:detail',article.pk)
    else:
        form = ArticleForm(initial=article.__dict__)
        # embed() 글 수정이 안됨

    context = {'form': form,
        'article': article}
    return render(request,'articles/form.html',context)


'''
* CREATE & UPDATE 는 html 파일 공유
Create 로직
1.GET
- 사용자가 데이터를 입력 할 수 있는 Form을 제공
2.POST
- 사용자가 보낸 새로운 글을 DB에 저장

Update 로직
1.GET
- 기존 사용자의 글이 입력된 Form 제공
2.POST
- 수정된 글을 DB에 저장
'''
@require_POST
def comments_create(request,article_pk):
    # article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm(request.POST) # request. POST 에는 사용자가 쓴 댓글정ㅇ보가 있습니다. 모델 class로부터 만드는 방법
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article_id=article_pk
        comment.save()
        return redirect('articles:detail',article_pk)

@require_POST
def comments_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk = comment_pk)
    comment.delete()
    return redirect('articles:detail',article_pk)