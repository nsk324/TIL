from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        max_length=10,
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class':'my-title',
                'placeholder':'Enter the title',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class':'my-content',
                'placeholder':'Enter thet content',
                'rows':5,
                'cols':50,
            }
        )
    )
    class Meta:
        model = Article
        fields = ('title','content', )
    
class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class':'my-comment',
                'placeholder':'Enter the title',
                'rows':5,
            }
        )
    )
    class Meta:
        model = Comment
        fields = ('content',)


# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=20,
#         label='제목',
#         widget=forms.TextInput(
#             attrs={
#                 'class':'my-title',
#                 'placeholder':'Enter the title!'
#             }
#         )
#     )
#     content = forms.CharField(
#         label='내용',
#         widget=forms.Textarea(
#             attrs={
#                 'class':'my-content',
#                 'placeholder':'Enter the title!',
#                 'rows':5,
#                 'cols':50,
#             }
#         )
#     )