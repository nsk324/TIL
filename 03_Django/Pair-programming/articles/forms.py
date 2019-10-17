from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title','content',)

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder':'제목입력하세요'
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'placeholder':'내용을 입력하세요'
                }
            )
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'placeholder':'내용입력하세요'
                }
            )
        }